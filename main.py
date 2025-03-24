from log_parser import extract_batch_details
from batch_monitor import classify_delay
from netcool_integration import send_netcool_alert
from xmatter_integration import escalate_xmatters_alert
from email_notifier import send_email_notification

LOG_FILE = "logs/tws_batch_logs.log"

def main():
    batch_data = extract_batch_details(LOG_FILE)
    delay_results = classify_delay(batch_data)

    for batch, details in delay_results.items():
        delay_percentage = details["delay_percentage"]
        status = details["status"]

        if status == "CRITICAL":
            escalate_xmatters_alert(batch, delay_percentage)
            send_email_notification(batch, status, delay_percentage)
        elif status == "MAJOR":
            send_netcool_alert(batch, delay_percentage)
            send_email_notification(batch, status, delay_percentage)
        elif status == "MINOR":
            print(f"[INFO] Minor delay detected for {batch}: {delay_percentage}%.")

if __name__ == "__main__":
    main()
