from datetime import datetime, timezone


def analyze_incident_logs(service_name: str) -> dict:
    """
    Simulates analyzing logs for a service.
    In production, this could query CloudWatch Logs, Splunk, Datadog, or OpenSearch.
    """
    return {
        "tool": "analyze_incident_logs",
        "service_name": service_name,
        "summary": f"Detected elevated 5xx errors and increased latency for {service_name}.",
        "possible_causes": [
            "Recent deployment introduced an application error",
            "Database connection pool exhaustion",
            "Upstream API timeout",
            "Insufficient pod replicas under load"
        ],
        "recommended_actions": [
            "Check latest deployment version",
            "Review error logs for stack traces",
            "Check database connection metrics",
            "Scale replicas if CPU or latency is high",
            "Prepare rollback if error rate continues"
        ],
        "severity": "high"
    }


def check_cloudwatch_alarm(alarm_name: str) -> dict:
    """
    Simulates checking a CloudWatch alarm.
    In production, this could call boto3 CloudWatch APIs.
    """
    return {
        "tool": "check_cloudwatch_alarm",
        "alarm_name": alarm_name,
        "state": "ALARM",
        "reason": "Average API latency exceeded threshold for 5 minutes.",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def create_jira_ticket(title: str, description: str, severity: str = "medium") -> dict:
    """
    Simulates creating a Jira ticket.
    In production, this could call Jira, ServiceNow, or GitHub Issues.
    """
    ticket_id = "DEVOPS-1001"

    return {
        "tool": "create_jira_ticket",
        "ticket_id": ticket_id,
        "title": title,
        "description": description,
        "severity": severity,
        "status": "created"
    }


def summarize_kubernetes_error(error_message: str) -> dict:
    """
    Simulates Kubernetes troubleshooting.
    """
    lower_error = error_message.lower()

    if "crashloopbackoff" in lower_error:
        cause = "The container is repeatedly crashing after startup."
        action = "Check container logs, environment variables, image version, and startup command."
    elif "imagepullbackoff" in lower_error:
        cause = "Kubernetes cannot pull the container image."
        action = "Verify image name, tag, registry credentials, and network access."
    elif "pending" in lower_error:
        cause = "The pod cannot be scheduled."
        action = "Check node capacity, taints, tolerations, affinity rules, and resource requests."
    else:
        cause = "The Kubernetes issue requires more context."
        action = "Check pod events, logs, deployment status, and cluster resource usage."

    return {
        "tool": "summarize_kubernetes_error",
        "error_message": error_message,
        "likely_cause": cause,
        "recommended_action": action
    }
