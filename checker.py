import requests
from config import WATCH, DISCORD_WEBHOOK

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
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": msg})

def run_check():
    results = fetch_availability()
    matches = [r for r in results if is_match(r)]

    if matches:
        best = sorted(matches, key=lambda x: WATCH["types"].index(x["type"]))[0]
        notify(f"🏕️ Fort Wilderness OPEN: {best['type']} {WATCH['start']} → {WATCH['end']}")
    else:
        print("No match found")

if __name__ == "__main__":
    run_check()
