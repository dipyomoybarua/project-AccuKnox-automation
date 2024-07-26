pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'github-credentials-id'
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: env.GITHUB_CREDENTIALS, url: 'https://github.com/dipyomoybarua/project-AccuKnox-automation.git'
            }
        }
        stage('Set up Python Environment') {
            steps {
                script {
                    // Install dependencies using a Python virtual environment
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pip install pyautogui pyscreeze
                    '''
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Debugging: List directory contents
                    bat '''
                        echo Checking contents of the workspace directory:
                        dir
                        echo Checking contents of the Deployment directory:
                        dir Deployment
                    '''

                    // Check if the Deployment directory exists
                    if (fileExists('Deployment')) {
                        bat '''
                            echo Applying Kubernetes manifests:
                            kubectl apply -f Deployment/
                        '''
                    } else {
                        error 'Deployment directory does not exist.'
                    }
                }
            }
        }
        stage('Port Forwarding') {
            steps {
                script {
                    // Debugging: List Kubernetes pods
                    bat '''
                        echo Retrieving frontend pod:
                        kubectl get pods -l app=frontend

                        echo Retrieving backend pod:
                        kubectl get pods -l app=backend
                    '''

                    // Set up port forwarding
                    bat '''
                        for /f "tokens=*" %%i in ('kubectl get pods -l app=frontend -o jsonpath="{.items[0].metadata.name}"') do set FRONTEND_POD=%%i
                        echo Frontend pod is %FRONTEND_POD%
                        kubectl port-forward %FRONTEND_POD% 8080:8080

                        for /f "tokens=*" %%i in ('kubectl get pods -l app=backend -o jsonpath="{.items[0].metadata.name}"') do set BACKEND_POD=%%i
                        echo Backend pod is %BACKEND_POD%
                        kubectl port-forward %BACKEND_POD% 8081:3000
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat '''
                        call venv\\Scripts\\activate
                        set PYTHONPATH=%WORKSPACE%
                        echo Running tests:
                        pytest -s -v --tb=short
                    '''
                }
            }
        }
        stage('Run Log Analyzer') {
            steps {
                script {
                    // Check if the log_analyzer.py file exists
                    if (fileExists('scripts/log_analyzer.py')) {
                        bat '''
                            call venv\\Scripts\\activate
                            set PYTHONPATH=%WORKSPACE%
                            echo Running log analyzer:
                            python scripts/log_analyzer.py
                        '''
                    } else {
                        error 'log_analyzer.py file does not exist.'
                    }
                }
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '**/reports/*', allowEmptyArchive: true
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
