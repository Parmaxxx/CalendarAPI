from conectApi import conectaApi
import datetime


service = conectaApi()

if service:
    now = datetime.datetime.utcnow().isoformat() + "Z"
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
    else:
        # Prints the ID, start, and name of the next 10 events
        for event in events:
            event_id = event["id"]
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(f"Event ID: {event_id}")
            print(f"Start: {start}")
            print(f"Summary: {event['summary']}")
            print()
else:
    print("Failed to connect to Google Calendar API.")
