"""Sequential streaming simulation for educational purposes."""

def process_events(events, validator):
    accepted = []
    rejected = []

    for event in events:
        is_valid, reason = validator(event)
        if is_valid:
            accepted.append(event)
            print(f"[ACCEPTED] {event['event_id']} - {event['event_type']}")
        else:
            rejected.append({"record": event, "reason": reason})
            print(f"[REJECTED] {reason}")

    return accepted, rejected
