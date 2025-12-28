import random
from datetime import datetime, timedelta

ips = ["192.168.1.10", "192.168.1.20", "10.0.0.5"]
actions = ["LOGIN FAIL", "LOGIN SUCCESS", "REQUEST"]

def generate_logs():
    current_time = datetime.now()

    with open("logs.txt", "w") as file:
        for i in range(50):
            ip = random.choice(ips)
            action = random.choice(actions)
            time = current_time + timedelta(seconds = i)
            file.write(f"{ip} {actions} {time.strftime('%H:%M:%S')}\n")

    if __name__ == "__main__" :
        generate_logs()
        print("Logs generated successfully")
