import yaml
from datetime import datetime, timedelta
from recon_db import get_batch_details
from log_parser import extract_batch_details
from netcool_integration import send_netcool_alert
from xmatter_integration import send_xmatters_alert
from email_notifier import send_email

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def calculate_expected_time(data_size):
    """Estimates expected time based on 10GB = 5 minutes."""
    return (data_size / 10) * 5  # Minutes

def analyze_batch_delays(batch_name, log_file):
    """Analyzes batch delays, classifies them, and triggers alerts."""
    batch_info = get_batch_details(batch_name)

    if not batch_info:  # If batch is not triggered
        print(f"Alert: {batch_name} has NOT been triggered.")
        return  # No logs to check

    batch_data = extract_batch_details(log_file)
    if batch_name not in batch_data:  
        print(f"Warning: {batch_name} logs not found.")
        return

    expected_time = calculate_expected_time(batch_info["data_size"])
    actual_time = batch_data[batch_name]["actual_time"]
    delay_percentage = ((actual_time - expected_time) / expected_time) * 100

    severity = None
    if delay_percentage > config["ALERT_THRESHOLDS"]["CRITICAL"]:
        severity = "Critical"
        send_xmatters_alert(batch_name, delay_percentage)
    elif delay_percentage > config["ALERT_THRESHOLDS"]["MAJOR"]:
        severity = "Major"
        send_netcool_alert(batch_name, delay_percentage)

    if severity:
        send_email(batch_name, severity, delay_percentage)

