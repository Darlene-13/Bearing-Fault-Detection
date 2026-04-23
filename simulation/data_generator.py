import csv
import random
from datetime import datetime, timedelta

LOG_FILE = "mine_sensor_log.csv"

def get_alert(p, d):
    if p >= 18.5 or d >= 10.0:
        return "DANGER"
    elif p >= 16.0 or d >= 5.0:
        return "WARNING"
    return "SAFE"

start_time = datetime.now()

with open(LOG_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "pressure_MPa", "displacement_mm", "alert"])

    for i in range(1000):
        # Random pressure between 8 and 22 MPa
        p = round(random.uniform(8.0, 22.0), 2)
        # Random displacement between 0 and 15 mm
        d = round(random.uniform(0.0, 15.0), 2)
        
        alert = get_alert(p, d)
        timestamp = start_time + timedelta(seconds=i * 2)

        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            p, d, alert
        ])

print("Generated 1000 readings →", LOG_FILE)