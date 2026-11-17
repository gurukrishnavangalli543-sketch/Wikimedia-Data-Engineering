"""Persist valid events and rejected-record details as JSON Lines."""
import json
from pathlib import Path

def write_jsonl(records, destination):
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\\n")

