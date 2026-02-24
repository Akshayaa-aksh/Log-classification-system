import re

def detect_level(log: str) -> str:
    log_lower = log.lower()
    if "critical" in log_lower:
        return "critical"
    elif "error" in log_lower:
        return "error"
    elif "warn" in log_lower:
        return "warn"
    else:
        return "info"


def detect_category(log: str) -> str:
    log_lower = log.lower()

    if "db" in log_lower or "database" in log_lower:
        return "database"
    elif "timeout" in log_lower or "latency" in log_lower:
        return "performance"
    elif "auth" in log_lower or "login" in log_lower:
        return "authentication"
    elif "network" in log_lower or "connection" in log_lower:
        return "network"
    else:
        return "unknown"


def detect_severity(level: str) -> int:
    mapping = {
        "critical": 5,
        "error": 4,
        "warn": 3,
        "info": 1
    }
    return mapping.get(level, 1)


def generate_summary(log: str) -> str:
    cleaned = re.sub(r"\[.*?\]", "", log)
    cleaned = re.sub(r"\d{4}-\d{2}-\d{2}.*?\d{2}:\d{2}:\d{2}", "", cleaned)
    words = cleaned.strip().split()
    return " ".join(words[:20])


def classify_log(log: str) -> dict:
    level = detect_level(log)
    category = detect_category(log)
    severity = detect_severity(level)

    return {
        "level": level,
        "category": category,
        "severity": severity,
        "isActionRequired": severity >= 4,
        "summary": generate_summary(log)
    }