from log_parser import extract_batch_details
from batch_monitor import analyze_batch_delays
from netcool_integration import send_netcool_alert
from xmatter_integration import escalate_xmatters_alert
from email_notifier import send_email

batch_data = extract_batch_details("logs/tws_batch_logs.log")
alerts = analyze_batch_delays(batch_data)

for severity, batch_name, delay_percentage in alerts:
    if severity == "Critical":
        escalate_xmatters_alert(batch_name, delay_percentage)
    if severity == "Major":
        send_netcool_alert(batch_name, delay_percentage)
    
    send_email(batch_name, severity, delay_percentage)
