import requests
import yaml

# Load config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

NETCOOL_API_URL = config["netcool"]["api_url"]
NETCOOL_API_KEY = config["netcool"]["api_key"]

def send_alert_to_netcool(severity, message):
    """Sends an alert to Netcool and returns the incident ID."""
    payload = {
        "severity": severity,
        "message": message,
        "source": "SmartAlertingSystem"
    }
    headers = {"Authorization": f"Bearer {NETCOOL_API_KEY}", "Content-Type": "application/json"}
    
    response = requests.post(NETCOOL_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        incident_id = response.json().get("incident_id")
        print(f"[Netcool] Alert Sent. Incident ID: {incident_id}")
        return incident_id
    else:
        print(f"[ERROR] Failed to send alert to Netcool: {response.text}")
        return None
