# batch_monitor.py - Identifies batch delays and sends alerts
from datetime import datetime
from config import BATCH_TIME_PER_10GB, ALERT_THRESHOLD_PERCENTAGE
from log_parser import extract_batch_details
from netcool_integration import send_netcool_alert
from email_notifier import send_email

def calculate_expected_time(data_size_gb):
    """Calculates expected batch execution time based on data size."""
    return (data_size_gb / 10) * BATCH_TIME_PER_10GB

def detect_batch_delay(log_file):
    """Checks batch delays and triggers alerts if needed."""
    batch_data = extract_batch_details(log_file)

    for batch_name, details in batch_data.items():
        if "end_time" in details:  # Ensure batch has completed
            expected_time = calculate_expected_time(details["data_size"])
            actual_time = details["actual_time"]
            delay_percentage = ((actual_time - expected_time) / expected_time) * 100

            if delay_percentage > ALERT_THRESHOLD_PERCENTAGE:
                alert_message = (
                    f"Batch '{batch_name}' delayed!\n"
                    f"Expected: {expected_time:.2f} min, Actual: {actual_time:.2f} min\n"
                    f"Delay: {delay_percentage:.2f}%"
                )

                print(alert_message)
                
                # Send alert to Netcool
                send_netcool_alert(batch_name, expected_time, actual_time, delay_percentage)

                # Notify production team
                send_email(batch_name, expected_time, actual_time, delay_percentage)
