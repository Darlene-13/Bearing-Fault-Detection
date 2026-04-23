import csv, time

def replay(file="mine_sensor_log.csv"):
    print("Replaying saved sensor data...\n")
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            alert = row["alert"]
            c = (
                "\033[91m" if alert == "DANGER" else
                "\033[93m" if alert == "WARNING" else
                "\033[92m"
            )
            reset = "\033[0m"
            print(c + "─────────────────────────────" + reset)
            print(f"  Time:        {row['timestamp']}")
            print(f"  Pressure:    {row['pressure_MPa']} MPa")
            print(f"  Convergence: {row['displacement_mm']} mm")
            print(c + f"  Alert:       {alert}" + reset)
            time.sleep(1)

if __name__ == "__main__":
    replay()