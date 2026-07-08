# 08-07-2026 | 08-07-2026

def triage_issue(ms, message):

    # 1 day = 24 hours * 60 minutes * 60 seconds * 1000 milliseconds
    SEVEN_DAYS_MS = 7 * 24 * 60 * 60 * 1000

    if ms < SEVEN_DAYS_MS:
        return "leave it"

    if "bump" in message.lower():
        return "close it"

    return "bump it"
