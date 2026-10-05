import re
import sqlite3
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
DATABASE = PROJECT_DIR / "visibility.db"
GENERATOR = PROJECT_DIR / "new_prompt_test_2.py"

result = subprocess.run(
    [sys.executable, str(GENERATOR)],
    cwd=PROJECT_DIR,
    stdout=subprocess.PIPE,
    text=True,
    check=True,
)

prompts = []

for line in result.stdout.splitlines():
    line = line.strip()

    # removing bullets or numbering
    line = re.sub(
        r"^(?:[-*•]|\d+[.)])\s*",
        "",
        line,
    )

    if line.endswith("?") and line not in prompts:
        prompts.append(line)

if not prompts:
    raise RuntimeError("No prompts found.")

# create db & save prompts
with sqlite3.connect(DATABASE) as connection:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt_text TEXT NOT NULL UNIQUE
        )
        """
    )

    connection.executemany(
        """
        INSERT OR IGNORE INTO prompts (prompt_text)
        VALUES (?)
        """,
        [(prompt,) for prompt in prompts],
    )

print("done")