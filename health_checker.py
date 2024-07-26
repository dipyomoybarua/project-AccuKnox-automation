import requests
from tests.fixtures.backend_base import BACKEND_URL
from tests.fixtures.frontend_base import FRONTEND_URL

def check_health(url):
    """Check the health of an application by sending a GET request."""
    try:
        response = requests.get(url)
        print(f"Checking {url} - Status Code: {response.status_code}, Response: {response.text}")
        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"
    except requests.RequestException as e:
        print(f"Error checking health for {url}: {e}")
        return "DOWN"

def get_urls():
    """Retrieve application URLs from fixtures."""
    return {
        "backend": BACKEND_URL,
        "frontend": FRONTEND_URL
    }
