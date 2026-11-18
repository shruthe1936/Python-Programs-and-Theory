processed = set()

def process_event(event_id):
    if event_id in processed:
        print("Duplicate event ignored")
    else:
        processed.add(event_id)
        print("Event processed")

process_event(101)
process_event(102)
process_event(101)