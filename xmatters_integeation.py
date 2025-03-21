import requests
import yaml
import time

# Load config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

XMATTERS_API_URL = config["xmatters"]["api_url"]
XMATTERS_API_KEY = config["xmatters"]["api_key"]
GROUP = config["xmatters"]["group"]
ESCALATION_TIME = config["xmatters"]["escalation_time"]

def send_alert_to_xmatters(severity, message, incident_id):
    """Sends an alert to xMatters for immediate action."""
    payload = {
        "group": GROUP,
        "severity": severity,
        "message": message,
        "incident_id": incident_id
    }
    headers = {"Authorization": f"Bearer {XMATTERS_API_KEY}", "Content-Type": "application/json"}
    
    response = requests.post(XMATTERS_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"[xMatters] Alert Sent to {GROUP}")
        escalate_if_no_response(incident_id)
    else:
        print(f"[ERROR] Failed to send alert to xMatters: {response.text}")

def escalate_if_no_response(incident_id):
    """Waits for response and escalates if not acknowledged."""
    time.sleep(ESCALATION_TIME * 60)  # Wait for acknowledgment

    # Check if the incident is resolved
    status_url = f"{XMATTERS_API_URL}/{incident_id}/status"
    headers = {"Authorization": f"Bearer {XMATTERS_API_KEY}"}
    response = requests.get(status_url, headers=headers)

    if response.status_code == 200 and response.json().get("status") == "resolved":
        print(f"[xMatters] Incident {incident_id} resolved. No escalation needed.")
    else:
        print(f"[xMatters] No response for Incident {incident_id}. Escalating...")
        escalation_payload = {"incident_id": incident_id, "action": "escalate"}
        requests.post(f"{XMATTERS_API_URL}/escalate", json=escalation_payload, headers=headers)
