import pytest
from health_checker import check_health, get_urls
from tests.utils.screenshot_utils import take_screenshot


@pytest.mark.parametrize("service, url", [
    ("backend", "https://jsonplaceholder.typicode.com/posts/1"),
    ("frontend", "https://httpbin.org/get")
])
def test_application_health(service, url):
    """Test the health of backend and frontend services."""
    try:
        status = check_health(url)
        print(f"{service} service status: {status}")
        assert status == "UP", f"{service} service is down. Status: {status}"
    except Exception as e:
        print(f"An error occurred during health check: {e}")
        take_screenshot(f"{service}_error")
        raise e
