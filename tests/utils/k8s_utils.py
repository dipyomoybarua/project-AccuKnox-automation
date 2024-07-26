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

def port_forward_pod(pod_name, local_port, remote_port):
    # Start the port-forward process
    command = [
        'kubectl', 'port-forward', pod_name,
        f'{local_port}:{remote_port}'
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait a bit to ensure the port-forwarding is set up
    time.sleep(5)
    
    return process