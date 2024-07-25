# tests/utils/k8s_utils.py
import subprocess
import time
import pytest

def get_pod_name(label_selector, namespace="default"):
    try:
        result = subprocess.run(
            ['kubectl', 'get', 'pods', '-n', namespace, '-l', label_selector, '-o', 'jsonpath={.items[0].metadata.name}'],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Failed to get pod name: {e.stderr.decode()}")

def port_forward_pod(pod_name, local_port, pod_port, namespace="default"):
    process = subprocess.Popen(
        ['kubectl', 'port-forward', pod_name, f'{local_port}:{pod_port}', '-n', namespace],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(10)  # Increased wait time for port-forward to establish
    return process
