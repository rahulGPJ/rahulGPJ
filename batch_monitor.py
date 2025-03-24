import yaml
from datetime import timedelta

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def calculate_expected_time(data_size):
    """Estimates expected time based on 10GB = 5 minutes."""
    return (data_size / 10) * 5  # Minutes

def analyze_batch_delays(batch_data):
    """Analyzes batch delays and classifies them into Minor, Major, or Critical."""
    alerts = []

    for batch_name, details in batch_data.items():
        expected_time = calculate_expected_time(details["data_size"])
        actual_time = details["actual_time"]
        delay_percentage = ((actual_time - expected_time) / expected_time) * 100

        if delay_percentage > config["ALERT_THRESHOLDS"]["CRITICAL"]:
            alerts.append(("Critical", batch_name, delay_percentage))
        elif delay_percentage > config["ALERT_THRESHOLDS"]["MAJOR"]:
            alerts.append(("Major", batch_name, delay_percentage))

    return alerts
