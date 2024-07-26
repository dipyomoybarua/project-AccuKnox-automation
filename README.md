# Overview of the QA Test Automation Project

We're diving into an exciting project that showcases how to seamlessly integrate and deploy both frontend and backend services onto the Kubernetes platform. But that's not all— we're also automating the testing process to ensure everything works together smoothly.

## Getting Started: What You'll Need

Before jumping in, make sure your toolkit is ready with these essentials:

- Python 3.12
- pip
- kubectl
- Minikube
- Git

## Navigating the Project Layout

Our project is neatly organized into folders for clarity:

- `backend/`: This is where the logic for the server side.
- `Deployment/`: This is home to the Kubernetes deployment configurations.
- `frontend/`: Everything client-facing lives here. The user interface components are developed in this folder.
- `tests/`: This is the one-stop folder for all testing scripts. It also contains helper utilities.

## Kickstarting the Project

### Grabbing the Code

Clone the repository with this quick command:

```bash
https://github.com/dipyomoybarua/project-AccuKnox-automation.git
cd qa-test
```

### Setting Up

1. Navigate to the `tests/` folder:

    ```bash
    cd tests
    ```

2. Load up the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. For dynamic screenshots, also run:

    ```bash
    pip install pyautogui pyscreeze
    ```

## Launching on Kubernetes

### Run Up Minikube

Start Minikube with:

```bash
minikube start
```

### Rolling Out the Services

1. Navigate to the `Deployment` directory:

    ```bash
    cd ../Deployment
    ```

2. Deploy both frontend and backend services:

    ```bash
    kubectl apply -f .
    ```

### Identify the Pods

1. Identify the frontend pod:

    ```bash
    kubectl get pods -l app=frontend
    ```

2. Identify the backend pods:

    ```bash
    kubectl get pods -l app=backend
    ```

### Establish Port Forwarding

1. Forward the frontend port:

    ```bash
    kubectl port-forward $(kubectl get pods -l app=frontend -o jsonpath="{.items[0].metadata.name}") 8080:8080
    ```

2. Forward the backend port:

    ```bash
    kubectl port-forward $(kubectl get pods -l app=backend -o jsonpath="{.items[0].metadata.name}") 8081:3000
    ```

## Initiating Automated Tests

1. Ensure both port forwarding commands are running in separate terminals.
2. Open a new terminal and navigate to the `tests/` directory:

    ```bash
    cd ../tests
    ```

3. Run the tests:

    ```bash
    python -m pytest -s -v --tb=short
    ```

## Capturing Moments with Screenshots

### Visual Debugging

Our custom utility in `screenshot_utils.py` ensures we've got proof of every test run, integrated into our test scripts.
 This makes for easy reference and troubleshooting.

## Final Checks

1. Double-check that Minikube is running smoothly before deployment.
2. Ensure port forwarding is correctly set up to allow for seamless communication.
3. Review the test results closely and make good use of screenshots for troubleshooting.