import os

WATCH = {
    "start": "2026-10-30",
    "end": "2026-11-02",
    "types": ["PREFERRED", "PREMIUM"],
}

# AT&T email-to-text address
EMAIL_TO = "3016978093@txt.att.net"

# Gmail credentials from GitHub Secrets
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

if not SMTP_USERNAME:
    raise ValueError("SMTP_USERNAME secret is missing")

if not SMTP_PASSWORD:
    raise ValueError("SMTP_PASSWORD secret is missing")
