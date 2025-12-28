FAILED_LIMIT = 5

def extract_ip(log_line):
    parts = log_line.split()
    for part in parts:
        if part.count('.') == 3:
            return part
    return None


def detect_bruteforce(logs):
    stack = {}     # IP -> list of failures
    alerts = []    # list of alert messages

    for log in logs:
        ip = extract_ip(log)
        if not ip:
            continue

        if "LOGIN_FAIL" in log:
            if ip not in stack:
                stack[ip] = []

            stack[ip].append("FAIL")

            if len(stack[ip]) > FAILED_LIMIT:
                alerts.append(f"BRUTE FORCE detected from {ip}")

        elif "LOGIN_SUCCESS" in log:
            stack[ip] = []   # reset stack on success

    return alerts   # ✅ MUST return list
