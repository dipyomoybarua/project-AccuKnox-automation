import requests
import pytest
from tests.utils.k8s_utils import get_pod_name, port_forward_pod

@pytest.fixture(scope="module")
def backend_response():
    pod_name = get_pod_name('app=backend')
    port_forward_process = port_forward_pod(pod_name, 8081, 3000)  

    try:
        response = requests.get("http://localhost:8081/greet")
        return response
    finally:
        port_forward_process.terminate()
