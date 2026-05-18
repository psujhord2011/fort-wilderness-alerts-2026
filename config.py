WATCH = {
    "start": "2026-10-30",
    "end": "2026-11-02",
    "adults": 3,
    "children": 1,
    "child_ages": [10],
    "types": ["PREMIUM", "PREFERRED", "FULL_HOOKUP"]
}

import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

if not SMTP_USERNAME:
    raise ValueError("SMTP_USERNAME secret is missing")
if not SMTP_PASSWORD:
    raise ValueError("SMTP_PASSWORD secret is missing")

EMAIL_TO = "3016978093@txt.att.net"
EMAIL_SUBJECT = "Fort Wilderness Alert"
EMAIL_BODY = "Campsite available for your selected dates!"
