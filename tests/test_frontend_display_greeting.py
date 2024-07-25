import pytest
from tests.fixtures.frontend_fixture import frontend_response

def test_frontend_displays_greeting(frontend_response):
    assert frontend_response.status_code == 200
    print(f"Response from frontend: {frontend_response.text}")  
    assert "Hello from the Backend!" in frontend_response.text
