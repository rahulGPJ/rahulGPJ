import sqlite3
import yaml

# Load DB Configuration
with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

DB_PATH = config["RECON_DB"]["PATH"]

def get_batch_details(batch_name):
    """Fetch batch execution status and expected data size from Recon DB."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = "SELECT status, data_size FROM batch_jobs WHERE batch_name = ?"
    cursor.execute(query, (batch_name,))
    result = cursor.fetchone()
    
    conn.close()
    if result:
        return {"status": result[0], "data_size": result[1]}
    return None  # If batch is not found, it hasn't started yet

