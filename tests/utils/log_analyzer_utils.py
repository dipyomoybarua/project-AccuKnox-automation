import re
from collections import Counter

def analyze_log(log_lines):
    """Analyze the log file for common patterns."""
    error_count = 0
    page_requests = Counter()
    ip_requests = Counter()

    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "GET .*?" HTTP/1\.1" (?P<status>\d{3})'
        )
    for line in log_lines:
        match = log_pattern.match(line)
        if match:
            ip, page, status = match.groups()
            ip_requests[ip] += 1
            page_requests[page] += 1
            if status == '404':
                error_count += 1

    return error_count, page_requests, ip_requests

def summarize_analysis(error_count, page_requests, ip_requests):
    """Generate a summary of the log analysis."""
    summary = []
    summary.append(f"Total 404 Errors: {error_count}")
    summary.append("\nMost Requested Pages:")
    if page_requests:
        for page, count in page_requests.most_common(10):
            summary.append(f"  {page}: {count} requests")
    else:
        summary.append("  No page requests found.")
    summary.append("\nIP Addresses with Most Requests:")
    if ip_requests:
        for ip, count in ip_requests.most_common(10):
            summary.append(f"  {ip}: {count} requests")
    else:
        summary.append("  No IP addresses found.")
    
    return "\n".join(summary)
