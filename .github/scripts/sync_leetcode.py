"""
Sync the user's accepted LeetCode submissions into the repo.

- First run (no state file): paginates the full `submissionList` history.
- Subsequent runs: uses `recentAcSubmissions` and stops at the last-seen timestamp.

For each surviving (titleSlug, lang) pair, fetches the actual submitted code
and the problem description, then writes:

  Tutorials/LeetCode/Questions/{id}-{Title}.md   (only if absent)
  Tutorials/LeetCode/Solutions/{id}-{Title}.{ext} (write/overwrite if newer)

State lives in .github/leetcode_sync_state.json and is committed alongside
the synced files so the next run knows where it left off.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
LEETCODE_DIR = ROOT / "Tutorials" / "LeetCode"
QUESTIONS_DIR = LEETCODE_DIR / "Questions"
SOLUTIONS_DIR = LEETCODE_DIR / "Solutions"
STATE_PATH = ROOT / ".github" / "leetcode_sync_state.json"

GRAPHQL_URL = "https://leetcode.com/graphql/"

# LeetCode lang slug -> file extension. Mirrors generate_leetcode_readme.py's
# LANG_MAP so synced files round-trip into the README index.
LANG_MAP: dict[str, str] = {
    "python3": ".py",
    "python": ".py",
    "rust": ".rs",
    "cpp": ".cpp",
    "golang": ".go",
    "java": ".java",
    "typescript": ".ts",
    "javascript": ".js",
    "mysql": ".sql",
    "mssql": ".sql",
    "oraclesql": ".sql",
    "postgresql": ".psql",
}

RECENT_AC_QUERY = """
query recentAcSubmissionList($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    title
    titleSlug
    timestamp
    lang
  }
}
"""

SUBMISSION_LIST_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String) {
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
    lastKey
    hasNext
    submissions {
      id
      title
      titleSlug
      statusDisplay
      lang
      timestamp
    }
  }
}
"""

SUBMISSION_DETAILS_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    lang { name verboseName }
    runtime
    memory
    question {
      questionId
      questionFrontendId
      title
      titleSlug
    }
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    content
    isPaidOnly
    topicTags { name }
  }
}
"""


@dataclass
class Submission:
    submission_id: int
    title: str
    title_slug: str
    lang: str
    timestamp: int


def build_session() -> requests.Session:
    session_cookie = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRF", "").strip()
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "tome-of-knowledge-sync/1.0 (+https://github.com/FurkanEdizkan/Tome-of-Knowledge)",
    })
    if session_cookie:
        s.cookies.set("LEETCODE_SESSION", session_cookie, domain="leetcode.com")
    if csrf:
        s.cookies.set("csrftoken", csrf, domain="leetcode.com")
        s.headers["x-csrftoken"] = csrf
    return s


def graphql(session: requests.Session, query: str, variables: dict, *, auth_required: bool = False) -> dict:
    resp = session.post(GRAPHQL_URL, json={"query": query, "variables": variables}, timeout=30)
    if resp.status_code in (401, 403):
        if auth_required:
            print(
                "ERROR: LeetCode rejected the request (HTTP %d). "
                "LEETCODE_SESSION appears expired or invalid — refresh the secret from "
                "browser devtools > Application > Cookies on leetcode.com." % resp.status_code,
                file=sys.stderr,
            )
            sys.exit(2)
        resp.raise_for_status()
    resp.raise_for_status()
    payload = resp.json()
    if "errors" in payload and payload["errors"]:
        raise RuntimeError(f"GraphQL errors: {payload['errors']}")
    return payload["data"]


def normalize_title(title: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_")


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {}
    return json.loads(STATE_PATH.read_text())


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def fetch_recent_ac(session: requests.Session, username: str, limit: int = 20) -> list[Submission]:
    data = graphql(session, RECENT_AC_QUERY, {"username": username, "limit": limit})
    out = []
    for item in data["recentAcSubmissionList"] or []:
        out.append(Submission(
            submission_id=int(item["id"]),
            title=item["title"],
            title_slug=item["titleSlug"],
            lang=item["lang"],
            timestamp=int(item["timestamp"]),
        ))
    return out


def iter_submission_list(session: requests.Session, *, max_pages: int | None) -> Iterable[Submission]:
    offset = 0
    last_key: str | None = None
    page = 0
    while True:
        if max_pages is not None and page >= max_pages:
            return
        data = graphql(
            session,
            SUBMISSION_LIST_QUERY,
            {"offset": offset, "limit": 20, "lastKey": last_key, "questionSlug": None},
            auth_required=True,
        )
        block = data.get("submissionList") or {}
        subs = block.get("submissions") or []
        for s in subs:
            if s.get("statusDisplay") != "Accepted":
                continue
            yield Submission(
                submission_id=int(s["id"]),
                title=s["title"],
                title_slug=s["titleSlug"],
                lang=s["lang"],
                timestamp=int(s["timestamp"]),
            )
        if not block.get("hasNext"):
            return
        last_key = block.get("lastKey")
        offset += len(subs)
        page += 1
        time.sleep(0.5)


def fetch_submission_code(session: requests.Session, submission_id: int) -> dict | None:
    data = graphql(session, SUBMISSION_DETAILS_QUERY, {"submissionId": submission_id}, auth_required=True)
    return data.get("submissionDetails")


def fetch_question(session: requests.Session, slug: str) -> dict | None:
    data = graphql(session, QUESTION_QUERY, {"titleSlug": slug})
    q = data.get("question")
    if not q or q.get("isPaidOnly"):
        return None
    return q


def html_to_text(html: str) -> str:
    """Convert LeetCode question HTML to the plain-text format used by existing
    Questions/*.md files: prose paragraphs, indented Example blocks, bulleted
    Constraints. Not perfect for every edge case but matches the in-repo style.
    """
    soup = BeautifulSoup(html or "", "lxml")

    for pre in soup.find_all("pre"):
        inner = pre.get_text()
        indented = "\n".join(("    " + line) if line.strip() else "" for line in inner.splitlines())
        pre.replace_with("\n" + indented.strip("\n") + "\n")

    for li in soup.find_all("li"):
        text = li.get_text(" ", strip=True)
        li.replace_with(f"- {text}\n")

    text = soup.get_text("\n")
    lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def render_question_md(question: dict) -> str:
    qid = question["questionFrontendId"]
    title = question["title"]
    body = html_to_text(question.get("content") or "")
    return f"# {qid}. {title}\n\n{body}\n"


def write_if_absent(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


def write_solution(path: Path, code: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not code.endswith("\n"):
        code += "\n"
    path.write_text(code)


def select_latest_per_pair(subs: Iterable[Submission]) -> dict[tuple[str, str], Submission]:
    """Keep only the newest submission per (titleSlug, lang)."""
    latest: dict[tuple[str, str], Submission] = {}
    for s in subs:
        key = (s.title_slug, s.lang)
        cur = latest.get(key)
        if cur is None or s.timestamp > cur.timestamp:
            latest[key] = s
    return latest


def collect_submissions(
    session: requests.Session,
    username: str,
    state: dict,
    *,
    force_backfill: bool,
    max_pages: int | None,
) -> list[Submission]:
    have_state = bool(state.get("submissions"))
    if force_backfill or not have_state:
        print("Mode: full backfill via submissionList")
        return list(iter_submission_list(session, max_pages=max_pages))

    last_synced_ts = max(
        (entry.get("timestamp", 0) for entry in state["submissions"].values()),
        default=0,
    )
    print(f"Mode: incremental (last synced ts = {last_synced_ts})")
    recent = fetch_recent_ac(session, username, limit=20)
    return [s for s in recent if s.timestamp > last_synced_ts]


def sync(username: str, *, force_backfill: bool, dry_run: bool, max_pages: int | None) -> int:
    QUESTIONS_DIR.mkdir(parents=True, exist_ok=True)
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)

    session = build_session()
    state = load_state()
    state.setdefault("username", username)
    state.setdefault("submissions", {})

    candidates = collect_submissions(
        session, username, state,
        force_backfill=force_backfill, max_pages=max_pages,
    )
    if not candidates:
        print("No new accepted submissions.")
        return 0

    latest = select_latest_per_pair(candidates)
    print(f"Found {len(candidates)} candidate submissions, {len(latest)} unique (problem, lang) pairs.")

    question_cache: dict[str, dict] = {}
    written = 0
    skipped = 0
    problems_touched: set[str] = set()

    for (slug, lang), sub in sorted(latest.items(), key=lambda kv: kv[1].timestamp):
        ext = LANG_MAP.get(lang)
        if ext is None:
            print(f"  skip {slug} [{lang}] — unsupported language")
            skipped += 1
            continue

        state_key = f"{slug}::{lang}"
        prev = state["submissions"].get(state_key, {})
        if prev.get("timestamp", 0) >= sub.timestamp and not force_backfill:
            skipped += 1
            continue

        if slug not in question_cache:
            q = fetch_question(session, slug)
            if q is None:
                print(f"  skip {slug} — paid-only or fetch failed")
                skipped += 1
                continue
            question_cache[slug] = q
            time.sleep(0.3)
        question = question_cache[slug]

        qid = question["questionFrontendId"]
        norm = normalize_title(question["title"])
        stem = f"{qid}-{norm}"

        q_path = QUESTIONS_DIR / f"{stem}.md"
        s_path = SOLUTIONS_DIR / f"{stem}{ext}"

        if dry_run:
            print(f"  [dry-run] would write {s_path.relative_to(ROOT)} (sub {sub.submission_id})")
            written += 1
            problems_touched.add(slug)
            continue

        details = fetch_submission_code(session, sub.submission_id)
        if not details or not details.get("code"):
            print(f"  skip {slug} [{lang}] — could not fetch code for submission {sub.submission_id}")
            skipped += 1
            continue
        time.sleep(0.3)

        if write_if_absent(q_path, render_question_md(question)):
            print(f"  + question {q_path.relative_to(ROOT)}")

        write_solution(s_path, details["code"])
        print(f"  + solution {s_path.relative_to(ROOT)} (sub {sub.submission_id})")
        written += 1
        problems_touched.add(slug)

        state["submissions"][state_key] = {
            "submission_id": sub.submission_id,
            "timestamp": sub.timestamp,
            "question_id": qid,
        }

    if not dry_run and written:
        if force_backfill or "last_full_backfill" not in state:
            state["last_full_backfill"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        save_state(state)

    print(f"\nSynced {written} submission file(s) across {len(problems_touched)} problem(s). Skipped {skipped}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync accepted LeetCode submissions into the repo.")
    parser.add_argument("--backfill", action="store_true", help="Force full submissionList pagination even if state exists.")
    parser.add_argument("--dry-run", action="store_true", help="List what would be written without touching the filesystem or fetching code.")
    parser.add_argument("--max-pages", type=int, default=None, help="Cap pagination pages (for testing).")
    args = parser.parse_args()

    username = os.environ.get("LEETCODE_USERNAME", "furkandedizkan").strip()
    if not username:
        print("LEETCODE_USERNAME is empty.", file=sys.stderr)
        return 2

    return sync(
        username,
        force_backfill=args.backfill,
        dry_run=args.dry_run,
        max_pages=args.max_pages,
    )


if __name__ == "__main__":
    sys.exit(main())
