def send_netcool_alert(batch_name, delay_percentage):
    """Logs alerts to Netcool for Major delays."""
    print(f"[Netcool] ALERT: Batch {batch_name} is delayed by {delay_percentage}%")
