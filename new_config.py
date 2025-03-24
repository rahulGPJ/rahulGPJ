# config.py - Stores global configurations

# Define batch thresholds (in minutes per 10GB of data)
BATCH_TIME_PER_10GB = 5  # Expected time for 10GB data

# Alert threshold (delay percentage)
ALERT_THRESHOLD_PERCENTAGE = 20  # Raise alert if delay > 20%

# Netcool API Endpoint
NETCOOL_API_URL = "https://netcool.example.com/api/alerts"

# xMatters API Endpoint
XMATTERS_API_URL = "https://xmatter.example.com/api/alerts"

# Email Configuration
EMAIL_RECIPIENTS = ["production_team@example.com"]
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_SENDER = "batch_alerts@example.com"
EMAIL_PASSWORD = "your_password"
