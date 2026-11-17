"""Read event records from a local JSON source."""
import json
from pathlib import Path

def load_events(source_path):
    path = Path(source_path)
    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)
    if not isinstance(records, list):
        raise ValueError("The input JSON must contain a list of event records.")
    return records
