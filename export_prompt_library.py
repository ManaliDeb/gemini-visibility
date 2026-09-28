import csv
import re
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).parent
GENERATOR = PROJECT_DIR / "new_prompt_test_2.py"
OUTPUT_CSV = PROJECT_DIR / "prompt_library.csv"


def clean_prompt(line: str) -> str:
    line = line.strip()

    line = re.sub(r"^(?:[-*•]|\d+[.)])\s*", "", line)

    return line.strip().strip('"')


result = subprocess.run(
    [sys.executable, str(GENERATOR)],
    cwd=PROJECT_DIR,
    capture_output=True,
    text=True,
    check=True,
)

prompts = []
seen = set()

for line in result.stdout.splitlines():
    prompt = clean_prompt(line)

    # this ignores warnings printed above the generated prompts.
    if not prompt.endswith("?"):
        continue

    normalized = prompt.casefold()

    if normalized not in seen:
        seen.add(normalized)
        prompts.append(prompt)

if not prompts:
    raise RuntimeError(
        "No prompts were detected in the generator output."
    )

with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(
        csv_file,
        fieldnames=["prompt_id", "prompt_text"],
    )
    writer.writeheader()

    for number, prompt in enumerate(prompts, start=1):
        writer.writerow(
            {
                "prompt_id": f"prompt_{number:03d}",
                "prompt_text": prompt,
            }
        )

print(f"Saved {len(prompts)} prompts to {OUTPUT_CSV}")