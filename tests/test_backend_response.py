import pytest
from tests.fixtures.backend_fixture import backend_response
from tests.utils.api_utils import extract_message

def test_backend_response(backend_response):
    assert backend_response.status_code == 200
    message = extract_message(backend_response)
    print(f"Response from backend: {message}")
    assert message == "Hello from the Backend!"
