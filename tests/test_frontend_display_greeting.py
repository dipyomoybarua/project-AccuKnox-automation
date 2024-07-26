import pytest
from tests.fixtures.frontend_fixture import frontend_response
from tests.utils.screenshot_utils import take_screenshot


def test_frontend_displays_greeting(frontend_response):
    try:
        assert frontend_response.status_code == 200
        print(f"Response from frontend: {frontend_response.text}")  
        assert "Hello from the Backend!" in frontend_response.text
        take_screenshot("frontend_success")
    except AssertionError as e:
        take_screenshot("frontend_failure")
        raise e

