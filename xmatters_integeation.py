# xmatter_integration.py - Escalates critical batch delays to xMatters

import requests
from config import XMATTERS_API_URL

def escalate_to_xmatters(batch_name, expected_time, actual_time, delay_percentage):
    """Escalates batch delay issues to xMatters when delay is critical (>50%)."""
    
    payload = {
        "incident": "CRITICAL_BATCH_DELAY",
        "batch_name": batch_name,
        "expected_time": f"{expected_time:.2f} min",
        "actual_time": f"{actual_time:.2f} min",
        "delay_percentage": f"{delay_percentage:.2f}%",
        "priority": "Critical",
        "notify": ["oncall_team@example.com"]
    }

    response = requests.post(XMATTERS_API_URL, json=payload)
    
    if response.status_code == 200:
        print(f"🚨 xMatters escalation triggered for {batch_name}")
    else:
        print(f"❌ Failed to escalate to xMatters: {response.status_code}")
