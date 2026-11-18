
def assess_severity(subject, body, priority):

    text = (subject + " " + body).lower()

    # Critical severity
    critical_words = [
        "server down",
        "system down",
        "complete outage",
        "all users",
        "business stopped",
        "data breach",
        "data loss",
        "security breach"
    ]

    # High severity
    high_words = [
        "server overheating",
        "network outage",
        "cannot access",
        "unable to access",
        "system failure",
        "multiple users",
        "critical"
    ]

    # Medium severity
    medium_words = [
        "error",
        "slow",
        "intermittent",
        "not working",
        "performance issue"
    ]

    if any(word in text for word in critical_words):
        severity = "Critical"

    elif any(word in text for word in high_words) or priority == "high":
        severity = "High"

    elif any(word in text for word in medium_words) or priority == "medium":
        severity = "Medium"

    else:
        severity = "Low"

    return severity
