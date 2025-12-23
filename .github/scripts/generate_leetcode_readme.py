from pathlib import Path
import re

ROOT = Path(".")
LEETCODE = ROOT / "Tutorials" / "LeetCode"

QUESTIONS_DIR = LEETCODE / "Questions"
SOLUTIONS_DIR = LEETCODE / "Solutions"
README_PATH = LEETCODE / "README.md"

LANG_MAP = {
    ".py": "Python",
    ".rs": "Rust",
    ".cpp": "C++",
    ".go": "Go",
    ".java": "Java",
    ".ts": "TypeScript",
}

def parse_question_filename(path):
    match = re.match(r"(\d+)[-_](.+)\.md", path.name)
    if not match:
        return None
    qid, title = match.groups()
    return qid, title.replace("_", " ")

def parse_solution_filename(path):
    match = re.match(r"(\d+)[-_](.+)\.(\w+)", path.name)
    if not match:
        return None
    qid, title, ext = match.groups()
    return qid, title.replace("_", " "), f".{ext}"

def generate_section():
    questions = {}

    for q in QUESTIONS_DIR.glob("*.md"):
        parsed = parse_question_filename(q)
        if parsed:
            qid, title = parsed
            questions[qid] = {
                "title": title,
                "question_path": q.relative_to(LEETCODE).as_posix(),
                "solutions": []
            }

    for s in SOLUTIONS_DIR.glob("*.*"):
        parsed = parse_solution_filename(s)
        if parsed:
            qid, _, ext = parsed
            if qid in questions and ext in LANG_MAP:
                questions[qid]["solutions"].append(
                    (LANG_MAP[ext], s.relative_to(LEETCODE).as_posix())
                )

    content = []
    for qid in sorted(questions, key=lambda x: int(x)):
        q = questions[qid]
        content.append(f"### {qid}. {q['title']}")
        content.append(f"- 📄 [Question]({q['question_path']})")
        if q["solutions"]:
            content.append("- 💻 Solutions:")
            for lang, path in sorted(q["solutions"]):
                content.append(f"  - [{lang}]({path})")
        content.append("")

    return "\n".join(content)

def update_readme():
    readme = README_PATH.read_text()
    new_section = generate_section()

    updated = re.sub(
        r"<!-- AUTO-GENERATED-START -->.*?<!-- AUTO-GENERATED-END -->",
        f"<!-- AUTO-GENERATED-START -->\n{new_section}\n<!-- AUTO-GENERATED-END -->",
        readme,
        flags=re.S
    )

    README_PATH.write_text(updated)

if __name__ == "__main__":
    update_readme()
