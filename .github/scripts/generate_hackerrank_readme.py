from pathlib import Path
import re

ROOT = Path(".")
HACKERRANK = ROOT / "Tutorials" / "HackerRank"

QUESTIONS_DIR = HACKERRANK / "Questions"
SOLUTIONS_DIR = HACKERRANK / "Solutions"
README_PATH = HACKERRANK / "README.md"

LANG_MAP = {
    ".py": "Python",
    ".rs": "Rust",
    ".cpp": "C++",
    ".go": "Go",
    ".java": "Java",
    ".ts": "TypeScript",
    ".sql": "SQL",
    ".psql": "PostgreSQL"
}

def normalize_title(raw_name):
    cleaned = raw_name.replace("_", " ").strip()
    return re.sub(r"\s+", " ", cleaned)

def slugify(raw_name):
    normalized = normalize_title(raw_name).lower()
    slug = re.sub(r"[^a-z0-9]", "", normalized)
    return slug

def parse_question_filename(path):
    if path.suffix != ".md":
        return None
    title = normalize_title(path.stem)
    slug = slugify(path.stem)
    if not slug:
        return None
    return slug, title

def parse_solution_filename(path):
    ext = path.suffix.lower()
    if ext not in LANG_MAP:
        return None
    slug = slugify(path.stem)
    if not slug:
        return None
    return slug, normalize_title(path.stem), ext

def generate_section():
    questions = {}

    for q in QUESTIONS_DIR.glob("*.md"):
        parsed = parse_question_filename(q)
        if parsed:
            slug, title = parsed
            questions[slug] = {
                "title": title,
                "question_path": q.relative_to(HACKERRANK).as_posix(),
                "solutions": []
            }

    for s in SOLUTIONS_DIR.glob("*.*"):
        parsed = parse_solution_filename(s)
        if parsed:
            slug, _, ext = parsed
            if slug in questions and ext in LANG_MAP:
                questions[slug]["solutions"].append(
                    (LANG_MAP[ext], s.relative_to(HACKERRANK).as_posix())
                )

    content = []
    for slug in sorted(questions, key=lambda x: questions[x]["title"].lower()):
        q = questions[slug]
        content.append(f"### {q['title']}")
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
