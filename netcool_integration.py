# netcool_integration.py - Sends delay alerts to Netcool

import requests
from config import NETCOOL_API_URL

def send_netcool_alert(batch_name, expected_time, actual_time, delay_percentage):
    """Sends alert to Netcool when a batch is delayed (>20%)."""
    
    payload = {
        "event_type": "BATCH_DELAY",
        "batch_name": batch_name,
        "expected_time": f"{expected_time:.2f} min",
        "actual_time": f"{actual_time:.2f} min",
        "delay_percentage": f"{delay_percentage:.2f}%",
        "severity": "High" if delay_percentage > 50 else "Medium"
    }

    response = requests.post(NETCOOL_API_URL, json=payload)
    
    if response.status_code == 200:
        print(f"✅ Netcool alert sent for {batch_name}")
    else:
        print(f"❌ Failed to send Netcool alert: {response.status_code}")
