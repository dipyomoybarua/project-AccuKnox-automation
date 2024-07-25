import requests
import pytest
from tests.utils.k8s_utils import get_pod_name, port_forward_pod

@pytest.fixture(scope="module")
def frontend_response():
    pod_name = get_pod_name('app=frontend')
    port_forward_process = port_forward_pod(pod_name, 8080, 8080)

    try:
        response = requests.get("http://localhost:8080")
        return response
    finally:
        port_forward_process.terminate()
