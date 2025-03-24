import re
from datetime import datetime

def extract_batch_details(log_file):
    """Reads logs and extracts batch details (start time, end time, and data size)."""
    with open(log_file, 'r') as file:
        logs = file.readlines()

    batch_data = {}

    for line in logs:
        start_match = re.search(r"\[(.*?)\] Job Started: (.*?), Data Size: (\d+)GB", line)
        end_match = re.search(r"\[(.*?)\] Job Completed: (.*?), Time Taken: (\d+)m (\d+)s", line)

        if start_match:
            timestamp, batch_name, data_size = start_match.groups()
            batch_data[batch_name] = {
                "start_time": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                "data_size": int(data_size)
            }

        if end_match:
            timestamp, batch_name, minutes, seconds = end_match.groups()
            batch_data[batch_name]["end_time"] = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            batch_data[batch_name]["actual_time"] = int(minutes) + int(seconds) / 60

    return batch_data
