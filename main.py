import os
from pathlib import Path

LINE = "Agenda: one bullet point. Duration: one hour. Outcome: another meeting."

def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
