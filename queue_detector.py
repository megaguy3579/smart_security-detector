REQUEST_LIMIT = 10

def extract_ip(log_line):
    parts = log_line.split()
    for part in parts:
        if part.count('.') == 3:
            return part
    return None


def detect_dos(logs):
    queue = {}      # IP -> list of requests
    alerts = []     # list of alert messages

    for log in logs:
        ip = extract_ip(log)
        if not ip:
            continue

        if "REQUEST" in log:
            if ip not in queue:
                queue[ip] = []

            queue[ip].append("REQ")

            if len(queue[ip]) > REQUEST_LIMIT:
                alerts.append(f"DoS attack detected from {ip}")

    return alerts    # ✅ ALWAYS returns a list
