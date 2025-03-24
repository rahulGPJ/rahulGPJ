import smtplib
import yaml

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def send_email(batch_name, severity, delay_percentage):
    """Sends email notification to production team."""
    subject = f"Batch Delay Alert: {batch_name} ({severity})"
    body = f"The batch '{batch_name}' is delayed by {delay_percentage:.2f}%."

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(config["EMAIL"]["SMTP_SERVER"], config["EMAIL"]["PORT"]) as server:
        server.starttls()
        server.login(config["EMAIL"]["SENDER"], config["EMAIL"]["PASSWORD"])
        server.sendmail(config["EMAIL"]["SENDER"], config["EMAIL"]["RECIPIENTS"], message)
