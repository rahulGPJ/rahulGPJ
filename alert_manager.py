# alert_manager.py - Detects batch delays and triggers alerts

from netcool_integration import send_netcool_alert
from xmatter_integration import escalate_to_xmatters
from email_notifier import send_email_notification

def handle_batch_delay(batch_name, expected_time, actual_time):
    """Detects batch delay and triggers appropriate alerts and notifications."""
    
    delay_percentage = ((actual_time - expected_time) / expected_time) * 100
    
    print(f"📊 Batch: {batch_name}, Expected: {expected_time} min, Actual: {actual_time} min, Delay: {delay_percentage:.2f}%")
    
    if delay_percentage > 20:
        # 🔔 Send alert to Netcool if delay > 20%
        send_netcool_alert(batch_name, expected_time, actual_time, delay_percentage)
    
    if delay_percentage > 50:
        # 🚨 Escalate to xMatters if delay > 50%
        escalate_to_xmatters(batch_name, expected_time, actual_time, delay_percentage)
        
        # 📩 Send email to production team
        send_email_notification(
            subject=f"🚨 Critical Delay in {batch_name}",
            body=f"The batch {batch_name} is delayed by {delay_percentage:.2f}%.\n"
                 f"Expected Time: {expected_time} min\n"
                 f"Actual Time: {actual_time} min\n"
                 f"Immediate attention is required!",
            recipients=["production_team@example.com"]
        )
