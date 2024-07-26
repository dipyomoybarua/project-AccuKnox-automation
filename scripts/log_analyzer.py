import requests
from tests.utils.log_analyzer_utils import analyze_log, summarize_analysis
from tests.fixtures.log_urls import LOG_URL
from tests.utils.screenshot_utils import take_screenshot


def fetch_log(log_url):
    """Fetch log file from a URL."""
    try:
        response = requests.get(log_url)
        response.raise_for_status()
        log_content = response.text
        if not log_content.strip():  # Check if the content is empty or whitespace
            print("No logs found in the URL.")
            take_screenshot("no_logs_found.png")
            return []
        return log_content.splitlines()
    except requests.exceptions.RequestException as e:
        take_screenshot("error_fetching_log.png")
        print(f"Error fetching log file: {e}")
        return []

def main():
    log_lines = fetch_log(LOG_URL)
    if not log_lines:
        print("No log data to analyze.")
        return

    error_count, page_requests, ip_requests = analyze_log(log_lines)
    summary = summarize_analysis(error_count, page_requests, ip_requests)
    
    print(summary)
    
    if not page_requests and not ip_requests:
        take_screenshot("no_log_data_found.png")

if __name__ == "__main__":
    main()
