import smtplib
from email.mime.text import MIMEText
import yaml

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def send_email_notification(batch_name, status, delay_percentage):
    """Sends an email alert to the production team."""
    subject = f"Batch Delay Alert: {batch_name} ({status})"
    body = f"Batch {batch_name} is delayed by {delay_percentage}%. Please take action."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config["EMAIL_SETTINGS"]["SENDER_EMAIL"]
    msg["To"] = config["EMAIL_SETTINGS"]["RECEIVER_EMAIL"]

    with smtplib.SMTP(config["EMAIL_SETTINGS"]["SMTP_SERVER"], config["EMAIL_SETTINGS"]["SMTP_PORT"]) as server:
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())

    print(f"[Email] Notification sent for {batch_name} ({status}).")
