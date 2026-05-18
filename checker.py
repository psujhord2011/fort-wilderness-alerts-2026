import requests
import smtplib
from email.message import EmailMessage

from config import WATCH, EMAIL_TO, SMTP_USERNAME, SMTP_PASSWORD


def fetch_availability():
    # Placeholder logic - replace with real Disney scraping later
    return [
        {"type": "PREMIUM", "start": "2026-10-30", "end": "2026-11-02"},
        {"type": "PREFERRED", "start": "2026-10-30", "end": "2026-11-02"},
    ]


def is_match(result):
    return (
        result["type"] in WATCH["types"]
        and result["start"] <= WATCH["start"]
        and result["end"] >= WATCH["end"]
    )


def notify(msg):
    print(msg)

    email = EmailMessage()
    email["From"] = SMTP_USERNAME
    email["To"] = EMAIL_TO
    email["Subject"] = "Fort Wilderness Alert"
    email.set_content(msg)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(email)


def run_check():
    results = fetch_availability()
    matches = [r for r in results if is_match(r)]

    if matches:
        best = sorted(matches, key=lambda x: WATCH["types"].index(x["type"]))[0]
        notify(
            f"Fort Wilderness OPEN: {best['type']} "
            f"{WATCH['start']} to {WATCH['end']}"
        )
    else:
        print("No match found")


if __name__ == "__main__":
    run_check()
