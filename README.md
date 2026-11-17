# Wikimedia Event Data Pipeline (Educational Prototype)

## Overview
This individual Python project demonstrates a simplified event-data pipeline inspired by the publicly documented concepts in Wikimedia's Event Platform. It illustrates ingestion, schema-style validation, streaming simulation, JSONL storage, and basic analysis.

**Scope:** This is an educational prototype using fictional sample events. It is not Wikimedia source code, does not connect to Wikimedia production services, and does not reproduce its infrastructure.

## Pipeline
1. **Ingestion:** reads event records from `data/sample_events.json`.
2. **Validation:** checks required fields and basic data types.
3. **Streaming simulation:** processes each event sequentially.
4. **Storage:** writes valid events to `output/valid_events.jsonl`.
5. **Analysis:** creates a summary report at `output/summary.json`.

## Requirements
- Python 3.9 or later
- No third-party packages are required.

## Run
From this project directory:

```bash
python main.py
```

The program prints a processing summary and creates the output files.

## Project structure
```text
Wikimedia_Event_Data_Pipeline/
├── data/
│   └── sample_events.json
├── output/
│   └── .gitkeep
├── pipeline/
│   ├── __init__.py
│   ├── ingestion.py
│   ├── validation.py
│   ├── streaming.py
│   ├── storage.py
│   └── analysis.py
├── main.py
├── requirements.txt
└── README.md
```

## Example output
The supplied sample contains valid and invalid records. The pipeline reports how many records were read, accepted, and rejected. Exact counts are determined by the sample file and validation rules.

## Limitations and future improvements
This prototype processes a local sample file and simulates streaming sequentially. A production system would require durable messaging infrastructure, schema governance, monitoring, retry and dead-letter handling, security controls, and scalable storage.

## References
- Otto, A. (2020) 'Wikimedia's Event Data Platform, or JSON is ok too'. Diff, 10 September. https://diff.wikimedia.org/2020/09/10/wikimedias-event-data-platform-or-json-is-ok-too/
- Wikimedia Foundation (n.d.) 'Event Platform'. Wikitech. https://wikitech.wikimedia.org/wiki/Event_Platform
- Wikimedia Foundation (n.d.) 'Event Platform/EventGate'. Wikitech. https://wikitech.wikimedia.org/wiki/Event_Platform/EventGate
- Wikimedia Foundation (n.d.) 'Event Platform/Schemas'. Wikitech. https://wikitech.wikimedia.org/wiki/Event_Platform/Schemas
