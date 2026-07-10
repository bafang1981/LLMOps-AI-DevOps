from pathlib import Path

KNOWLEDGE_FILE = Path("data/devops_knowledge.txt")


def search_knowledge_base(question: str) -> dict:
    if not KNOWLEDGE_FILE.exists():
        return {
            "found": False,
            "context": "",
            "source": "data/devops_knowledge.txt"
        }

    content = KNOWLEDGE_FILE.read_text(encoding="utf-8")
    question_lower = question.lower()

    matched_lines = []
    for line in content.splitlines():
        if any(word in line.lower() for word in question_lower.split() if len(word) > 3):
            matched_lines.append(line)

    if not matched_lines:
        return {
            "found": False,
            "context": "No matching context found in local knowledge base.",
            "source": "data/devops_knowledge.txt"
        }

    return {
        "found": True,
        "context": " ".join(matched_lines),
        "source": "data/devops_knowledge.txt"
    }
