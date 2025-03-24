import yaml
from datetime import timedelta
from log_parser import extract_batch_details

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def calculate_expected_time(data_size):
    """Estimate batch processing time (5 mins per 10GB)."""
    return (data_size / 10) * 5

def classify_delay(batch_data):
    """Classifies batch job delays as Minor, Major, or Critical."""
    delay_results = {}

    for batch, details in batch_data.items():
        expected_time = calculate_expected_time(details["data_size"])
        actual_time = details["actual_time"]
        delay_percentage = ((actual_time - expected_time) / expected_time) * 100

        if delay_percentage > config["ALERT_THRESHOLD"]["CRITICAL"]:
            status = "CRITICAL"
        elif delay_percentage > config["ALERT_THRESHOLD"]["MAJOR"]:
            status = "MAJOR"
        elif delay_percentage > config["ALERT_THRESHOLD"]["MINOR"]:
            status = "MINOR"
        else:
            status = "NORMAL"

        delay_results[batch] = {"delay_percentage": delay_percentage, "status": status}

    return delay_results
