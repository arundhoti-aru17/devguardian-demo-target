from pathlib import Path

# ==========================================================
# DevGuardian Demo Target Structure Generator
# ==========================================================

PROJECT_ROOT = Path.cwd()

folders = [
    ".github",
    ".github/workflows",
]

files = {
    "app.py": '''def greet():
    return "Hello DevGuardian!"
''',

    "test_app.py": '''from app import greet


def test_greet():
    assert greet() == "Hello DevGuardian!"
''',

    "requirements.txt": '''pytest
''',

    ".gitignore": '''__pycache__/
*.py[cod]
.pytest_cache/
.venv/
venv/
env/
''',

    "README.md": '''# DevGuardian Demo Target

This repository acts as the **patient** for DevGuardian AI.

It contains intentionally broken branches that DevGuardian will diagnose and fix.

## Purpose

- Simulate CI/CD failures
- Generate GitHub Actions logs
- Test DevGuardian AI agents
''',

    ".github/workflows/ci.yml": '''name: Python CI

on:
  push:
    branches:
      - main

jobs:
  test:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          pytest
'''
}


def create_structure():
    print("=" * 60)
    print("Creating DevGuardian Demo Target")
    print("=" * 60)

    # Create folders
    for folder in folders:
        path = PROJECT_ROOT / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created: {folder}")

    # Create files
    for file_path, content in files.items():
        file = PROJECT_ROOT / file_path

        if not file.exists():
            file.write_text(content, encoding="utf-8")
            print(f"📄 Created: {file_path}")
        else:
            print(f"⏩ Skipped (already exists): {file_path}")

    print("\n✅ Demo Target project created successfully!")


if __name__ == "__main__":
    create_structure()