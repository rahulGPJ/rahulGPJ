import json
import time
import yaml
from netcool_integration import send_alert_to_netcool
from xmatters_integration import send_alert_to_xmatters

# Load config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Load alert rules
with open("alert_rules.json", "r") as file:
    alert_rules = json.load(file)

log_file_path = config["log_file"]

def check_logs():
    """Monitors logs in real-time and triggers alerts for critical issues."""
    print("Monitoring logs for issues...")
    
    with open(log_file_path, "r") as file:
        file.seek(0, 2)  # Move to the end of the file

        while True:
            line = file.readline()
            if not line:
                time.sleep(2)  # Wait before checking new lines
                continue
            
            print(f"Log: {line.strip()}")

            # Check log severity
            for severity, keywords in alert_rules.items():
                if any(keyword in line for keyword in keywords):
                    print(f"[ALERT] {severity} issue detected: {line.strip()}")
                    
                    # Send alert to Netcool
                    incident_id = send_alert_to_netcool(severity, line.strip())

                    # Notify xMatters
                    send_alert_to_xmatters(severity, line.strip(), incident_id)
                    break  # Stop checking after first match

if __name__ == "__main__":
    check_logs()
