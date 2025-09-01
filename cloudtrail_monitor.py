import boto3
from datetime import datetime, timedelta

# Initialize CloudTrail client
client = boto3.client('cloudtrail', region_name='eu-west-2')  # UK region

# Define the time range (last 24 hours)
end_time = datetime.now()
start_time = end_time - timedelta(days=1)

# Retrieve the most recent events
try:
    response = client.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
        MaxResults=10
    )

    events = response.get('Events', [])
    if not events:
        print("[INFO] No CloudTrail events found in the last 24 hours.")
    else:
        print("[INFO] Recent CloudTrail events in the last 24 hours:\n")
        for event in events:
            print(f"Event Name: {event.get('EventName', 'N/A')}")
            print(f"Username: {event.get('Username', 'N/A')}")
            print(f"Time: {event.get('EventTime', 'N/A')}")
            print(f"Source IP: {event.get('SourceIPAddress', 'N/A')}")
            print("-" * 40)

except client.exceptions.ClientError as e:
    print(f"[ERROR] {e}")
