"""Run the educational Wikimedia-inspired event pipeline."""
import json
from pathlib import Path

from pipeline.ingestion import load_events
from pipeline.validation import validate_event
from pipeline.streaming import process_events
from pipeline.storage import write_jsonl
from pipeline.analysis import build_summary

ROOT = Path(__file__).resolve().parent

def main():
    source = ROOT / "data" / "sample_events.json"
    output_dir = ROOT / "output"

    print("Wikimedia-inspired Event Data Pipeline")
    print("--------------------------------------")

    events = load_events(source)
    print(f"Ingested {len(events)} event records.\n")

    accepted, rejected = process_events(events, validate_event)

    write_jsonl(accepted, output_dir / "valid_events.jsonl")
    write_jsonl(rejected, output_dir / "rejected_events.jsonl")

    summary = build_summary(len(events), accepted, rejected)
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    print("\nProcessing summary")
    print(json.dumps(summary, indent=2))
    print(f"\nOutput files saved in: {output_dir}")

if __name__ == "__main__":
    main()
