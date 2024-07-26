import pytest
import requests
from tests.utils.log_analyzer_utils import analyze_log, summarize_analysis
from tests.fixtures.log_urls import LOG_URL
from tests.utils.screenshot_utils import take_screenshot


@pytest.fixture(scope='module')
def log_lines():
    """Fixture to fetch log lines from the URL, scoped to the module level."""
    try:
        response = requests.get(LOG_URL)
        response.raise_for_status()
        log_content = response.text
        if not log_content.strip():  # Check if the content is empty or whitespace
            return []
        return log_content.splitlines()
    except requests.exceptions.RequestException as e:
        take_screenshot("error_fetching_log.png")
        pytest.fail(f"Error fetching log file: {e}")

def test_analyze_log(log_lines):
    """Test the analyze_log function."""
    try:
        error_count, page_requests, ip_requests = analyze_log(log_lines)
        # Adjust these assertions based on expected results
        assert isinstance(error_count, int)
        assert isinstance(page_requests, dict)
        assert isinstance(ip_requests, dict)
    except AssertionError as e:
        take_screenshot("test_analyze_log_failure.png")
        raise e

def test_summarize_analysis(log_lines):
    """Test the summarize_analysis function."""
    try:
        error_count, page_requests, ip_requests = analyze_log(log_lines)
        summary = summarize_analysis(error_count, page_requests, ip_requests)
        # Basic checks to ensure summary contains expected text
        assert "Total 404 Errors:" in summary
        assert "Most Requested Pages:" in summary
        assert "IP Addresses with Most Requests:" in summary
    except AssertionError as e:
        take_screenshot("test_summarize_analysis_failure.png")
        raise e
