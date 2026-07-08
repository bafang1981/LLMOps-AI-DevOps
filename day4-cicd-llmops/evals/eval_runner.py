import json
import sys
from pathlib import Path

EVAL_FILE = Path("evals/test_questions.json")

def main():
    if not EVAL_FILE.exists():
        print("Evaluation file not found.")
        sys.exit(1)

    with open(EVAL_FILE, "r", encoding="utf-8") as file:
        tests = json.load(file)

    failures = []

    for test in tests:
        answer = test["answer"].lower()
        expected_keywords = test["expected_keywords"]

        missing = [
            keyword for keyword in expected_keywords
            if keyword.lower() not in answer
        ]

        if missing:
            failures.append({
                "question": test["question"],
                "missing_keywords": missing
            })

    if failures:
        print("Evaluation failed.")
        for failure in failures:
            print(failure)
        sys.exit(1)

    print("All evaluation checks passed.")

if __name__ == "__main__":
    main()
