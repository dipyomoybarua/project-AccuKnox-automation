import requests
import pytest
from tests.utils.k8s_utils import get_pod_name, port_forward_pod
import time

@pytest.fixture(scope="module")
def frontend_response():
    pod_name = get_pod_name('app=frontend')
    port_forward_process = port_forward_pod(pod_name, 8081, 8080)

    try:
        # Allow some time for the port-forwarding to establish
        time.sleep(5)
        response = requests.get("http://localhost:8081")
        if response.status_code == 200:
            return response
        else:
            pytest.fail(f"Request failed with status code: {response.status_code}")
    finally:
        # Terminate port-forward process
        port_forward_process.terminate()
        port_forward_process.wait()  # The process is properly cleaned up
