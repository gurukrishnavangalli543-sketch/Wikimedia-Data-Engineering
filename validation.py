"""Basic schema-style validation for incoming event records."""
from datetime import datetime

REQUIRED_FIELDS = {"event_id", "event_type", "timestamp", "user_id", "page"}
ALLOWED_EVENT_TYPES = {"page_view", "search", "edit"}

def validate_event(event):
    if not isinstance(event, dict):
        return False, "Record must be a JSON object."

    missing = REQUIRED_FIELDS - event.keys()
    if missing:
        return False, "Missing required field(s): " + ", ".join(sorted(missing))

    if not all(isinstance(event[field], str) and event[field].strip()
               for field in REQUIRED_FIELDS):
        return False, "All required fields must be non-empty strings."

    if event["event_type"] not in ALLOWED_EVENT_TYPES:
        return False, f"Unsupported event_type: {event['event_type']}"

    try:
        datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        return False, "timestamp must be an ISO 8601 date-time."

    return True, "Valid"
