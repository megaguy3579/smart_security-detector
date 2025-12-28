def extract_ip(log_line):
    """Extract IP dynamically from any position in a log line"""
    parts = log_line.split()
    for part in parts:
        if part.count('.') == 3:  # simple check for IPv4
            return part
    return None


def top_attacking_ips(logs):
    """
    Count number of activities per IP and return a sorted list of tuples:
    (IP, count) in descending order
    """
    count = {}

    for log in logs:
        ip = extract_ip(log)
        if not ip:
            continue

        count[ip] = count.get(ip, 0) + 1

    # Sort by number of activities descending
    sorted_ips = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_ips   # ✅ always returns a list
