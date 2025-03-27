import time
from batch_monitor import analyze_batch_delays

BATCHES_TO_MONITOR = ["Batch_A", "Batch_B", "Batch_C"]
LOG_FILE_PATH = "logs/tws_batch_logs.log"

while True:
    for batch in BATCHES_TO_MONITOR:
        analyze_batch_delays(batch, LOG_FILE_PATH)
    time.sleep(900)  # Run every 15 minutes
