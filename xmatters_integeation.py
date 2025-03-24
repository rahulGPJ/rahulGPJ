import requests
import yaml

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def escalate_xmatters_alert(batch_name, delay_percentage):
    """Escalates issues to xMatters using REST API."""
    payload = {
        "recipients": ["Production_Team"],
        "properties": {
            "batchName": batch_name,
            "delayPercentage": delay_percentage,
            "severity": "Critical"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config['XMATTERS']['API_KEY']}"
    }

    requests.post(config["XMATTERS"]["URL"], json=payload, headers=headers)
