from collections import Counter
from datetime import datetime
from log_classifier import classify_log


class LogAggregator:

    def __init__(self):
        self.logs = []
        self.counter = Counter()

    def add_log(self, raw_log: str):
        structured = classify_log(raw_log)

        structured["timestamp"] = datetime.now()
        self.logs.append(structured)

        key = structured["summary"]
        self.counter[key] += 1

        return structured

    def get_top_frequent(self, limit=5):
        return self.counter.most_common(limit)

    def get_high_severity_logs(self):
        return [log for log in self.logs if log["severity"] >= 4]

    def detect_spike(self, threshold=3):
        spikes = []
        for summary, count in self.counter.items():
            if count >= threshold:
                spikes.append({
                    "summary": summary,
                    "count": count,
                    "alert": True
                })
        return spikes