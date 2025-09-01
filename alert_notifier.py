import boto3
from datetime import datetime, timedelta


client = boto3.client('cloudtrail')


SUSPICIOUS_EVENTS = [
    'CreateUser',
    'DeleteUser',
    'AttachUserPolicy',
    'DeleteBucket',
    'PutBucketPolicy',
    'UpdateAssumeRolePolicy',
]


end_time = datetime.now()
start_time = end_time - timedelta(days=1)


response = client.lookup_events(
    StartTime=start_time,
    EndTime=end_time,
    MaxResults=50
)

events = response.get('Events', [])

if not events:
    print("[INFO] No CloudTrail events found in the last 24 hours.")
else:
    print("[INFO] Checking recent CloudTrail events for suspicious activity...\n")
    for event in events:
        event_name = event.get('EventName', 'N/A')
        username = event.get('Username', 'N/A')
        source_ip = event.get('SourceIPAddress', 'N/A')
        event_time = event.get('EventTime', 'N/A')

        if event_name in SUSPICIOUS_EVENTS:
            print(" SUSPICIOUS EVENT DETECTED! ")
            print(f"Event Name: {event_name}")
            print(f"Username: {username}")
            print(f"Source IP: {source_ip}")
            print(f"Time: {event_time}")
            print("----------------------------------------")
