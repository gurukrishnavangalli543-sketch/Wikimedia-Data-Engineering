"""Create a compact summary of processed events."""
from collections import Counter

def build_summary(total, accepted, rejected):
    event_counts = Counter(event["event_type"] for event in accepted)
    rejection_reasons = Counter(item["reason"] for item in rejected)

    return {
        "records_read": total,
        "valid_records": len(accepted),
        "rejected_records": len(rejected),
        "valid_events_by_type": dict(sorted(event_counts.items())),
        "rejection_reasons": dict(sorted(rejection_reasons.items()))
    }
