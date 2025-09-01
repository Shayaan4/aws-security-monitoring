**AWS Security Monitoring**

This project is a Python-based system that monitors AWS CloudTrail events and alerts on suspicious activity. It’s a lightweight way to simulate security monitoring like what a SOC (Security Operations Center) would do.

**Features**

\-Checks recent CloudTrail events for user activity.

\-Alerts on suspicious actions like IAM changes or unusual login attempts.

\-Displays events in a readable format in the console.

\-Uses Python and AWS APIs to fetch and analyze the data.

**Files**

**cloudtrail_monitor.py** – Monitors CloudTrail events and prints recent activity.

**alert_notifier.py** – Sends alerts when suspicious events are detected.

**requirements.txt** – Lists Python libraries needed (like ```boto3```).


**Setup**

1)Install Python 3.13 or higher.

2)Install dependencies by running: ```pip install -r requirements.txt.```

3)Configure AWS CLI with your access key, secret, and region using ```aws configure.```

**Usage**

1.Run the CloudTrail monitor:

```python cloudtrail_monitor.py```


2.Run the alert notifier if you want to receive alerts:

```python alert_notifier.py```

**Skills Demonstrated**

1)Cloud security monitoring using AWS CloudTrail.

2)Python scripting and automation.

3)Real-time alerting and log analysis.

4)AWS IAM and permissions management.
