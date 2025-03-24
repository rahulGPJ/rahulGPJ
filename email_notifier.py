# email_notifier.py - Sends email notifications for critical delays

import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD

def send_email_notification(subject, body, recipients):
    """Sends an email notification to the production team."""
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(recipients)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, recipients, msg.as_string())
        print("📩 Email notification sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
