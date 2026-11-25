import os
from pathlib import Path

SETUP = "Our meeting's one decision: schedule another meeting"
TWIST = "to decide what the email should have said."
LINE = SETUP + " " + TWIST

def main():
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
