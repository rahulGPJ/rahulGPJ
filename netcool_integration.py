import requests
import yaml

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def send_netcool_alert(batch_name, delay_percentage):
    """Logs alerts to Netcool using REST API."""
    payload = {
        "alertType": "Batch Delay",
        "batchName": batch_name,
        "delayPercentage": delay_percentage,
        "severity": "Major"
    }

    headers = {"Content-Type": "application/json"}
    auth = (config["NETCOOL"]["USERNAME"], config["NETCOOL"]["PASSWORD"])

    requests.post(config["NETCOOL"]["URL"], json=payload, headers=headers, auth=auth)
