from log_generator import generate_logs
from log_reader import read_logs
from stack_detector import detect_bruteforce
from queue_detector import detect_dos
from alerts_manager import save_alerts
from stats import top_attacking_ips

def main():
    print(">> Generate logs...")
    generate_logs()

    print(">> Reading logs...")
    logs = read_logs()

    print(">> Detecting brute force attacks(STACK)...")
    brute_alerts = detect_bruteforce(logs)

    print(">> Detecting Dos attacks(QUEUE)...")
    dos_alerts = detect_dos(logs)

    #combine all alerts
    all_alerts = []
    brute_alerts = detect_bruteforce(logs)
    if brute_alerts :
        all_alerts.extend(brute_alerts)
    dos_alerts = detect_dos(logs)
    if dos_alerts :
        all_alerts.extend(dos_alerts)

    print("Alerts found :", all_alerts)
    save_alerts(all_alerts)

    print(">> Alerts found:")
    if all_alerts :
        for alert in all_alerts :
            print(alert)
    else :
        print("No suspicious activity detected.")

    print("\n TOP ATTACKING IPs:")
    top_ips = top_attacking_ips(logs)
    for ip, count in top_ips :
        print(f"{ip} --> {count} activities")

if __name__ == "__main__" :
    main()
