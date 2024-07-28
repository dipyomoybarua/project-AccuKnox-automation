# Overview of the QA Test Automation Project

Get into exciting journey with me as we seamlessly integrate and deploy both frontend and backend services onto the Kubernetes platform. But that’s not all. We're also automating the testing process. This ensures everything works together smoothly.

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
- `scripts/`: Contains scripts for the tasks, which includes the log analyzer.

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

3. For screenshot functionality, install additional packages:

    ```bash
    pip install mss
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
    kubectl port-forward $(kubectl get pods -l app=frontend -o jsonpath="{.items[0].metadata.name}") ${LOCAL_FRONTEND_PORT}:${REMOTE_FRONTEND_PORT}
    ```

2. Forward the backend port:

    ```bash
    kubectl port-forward $(kubectl get pods -l app=backend -o jsonpath="{.items[0].metadata.name}") ${LOCAL_BACKEND_PORT}:${REMOTE_BACKEND_PORT}

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

### Running the Log Analyzer Script

The log analyzer script helps to analyze log files and summarize useful information. Follow these steps to run the script:

1. Navigate to the project root directory:

    ```bash
    cd ../qa-test
    ```

2. Set the `PYTHONPATH` environment variable:

    ```powershell
    $env:PYTHONPATH="path\to\your\project\root"
    ```

3. Run the log analyzer script:

    ```powershell
    python .\scripts\log_analyzer.py
    ```
### Handling No Logs or Errors

If no logs are found at the specified URL or if there are errors in fetching the logs, the script will handle it gracefully and take a screenshots.

## Jenkins Pipeline Integration

The Jenkins pipeline automates building deploying and testing our project. Ensure Jenkins is properly configured with necessary plugins and credentials.

### Configuring Jenkins

1. **Create New Pipeline Job**:
 - Go to Jenkins Dashboard. Click on “New Item” Select “Pipeline” and name it.

2. **Configure Source Code Management**:
 - Choose “GitHub project” and enter `https://github.com/dipyomoybarua/project-AccuKnox-automation.git`. Add GitHub credentials in `Manage Jenkins` section.

3. **Configure Pipeline**:
 - Choose “Pipeline script”. Enter the groovy script. Give the `Jenkinsfile` code.

4. **Configure Environment Variables**:
 - Set necessary environment variables. Examples include `GITHUB_CREDENTIALS`.

5. **Run the Pipeline**:
 - Save and run the pipeline job.

## Final Checks

1. Double-check that Minikube is running smoothly before deployment.
2. Ensure port forwarding is correctly set up to allow for seamless communication.
3. Review the test results closely and make good use of screenshots for troubleshooting.