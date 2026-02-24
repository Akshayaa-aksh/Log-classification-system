from log_aggregator import LogAggregator
from incident_agent import IncidentAgent


def simulate_logs(aggregator):

    logs = [
        "[ERROR] 2026-02-20 10:32:12 DB connection timeout after 5000ms",
        "[WARN] 2026-02-20 10:35:12 High API latency detected",
        "[ERROR] 2026-02-20 10:36:12 DB connection timeout after 5000ms",
        "[ERROR] 2026-02-20 10:37:12 DB connection timeout after 5000ms",
        "[CRITICAL] 2026-02-20 10:38:12 Authentication failure for admin"
    ]

    for log in logs:
        structured = aggregator.add_log(log)
        print("Processed Log:", structured)


def main():

    aggregator = LogAggregator()
    agent = IncidentAgent(aggregator)

    simulate_logs(aggregator)

    print("\n--- Incident Report ---")
    print(agent.generate_incident_report())


if __name__ == "__main__":
    main()