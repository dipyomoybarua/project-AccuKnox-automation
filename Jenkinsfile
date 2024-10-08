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
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r tests\\requirements.txt
                        pip show mss
                    '''
                }
            }
        }

        stage('Verify Deployment Directory') {
            steps {
                dir('Deployment') {
                    bat 'dir'
                }
            }
        }

        stage('Set File Permissions') {
            steps {
                script {
                    bat '''
                        icacls "Deployment\\backend-deployment.yaml" /grant Users:(R)
                        icacls "Deployment\\frontend-deployment.yaml" /grant Users:(R)
                    '''
                }
            }
        }

        stage('Workspace Path') {
            steps {
                bat 'echo %WORKSPACE%'
            }
        }

        stage('Create Deployment Directory') {
            steps {
                bat '''
                    if not exist Deployment (
                        mkdir Deployment
                        echo Directory created
                    ) else (
                        echo Directory already exists
                    )
                '''
            }
        }

        stage('Ensure Screenshots Directory') {
            steps {
                bat '''
                    if not exist screenshots (
                        mkdir screenshots
                        echo Screenshots directory created
                    ) else (
                        echo Screenshots directory already exists
                    )
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    bat '''
                        echo Checking contents of the workspace directory:
                        dir
                        echo Checking contents of the Deployment directory:
                        dir Deployment
                    '''

                    if (fileExists('Deployment/backend-deployment.yaml') && fileExists('Deployment/frontend-deployment.yaml')) {
                        bat '''
                            echo Applying Kubernetes manifests:
                            kubectl apply -f Deployment/
                        '''
                    } else {
                        error 'Deployment directory is empty or does not contain valid Kubernetes manifest files.'
                    }
                }
            }
        }

        stage('Port Forwarding') {
            steps {
                script {
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
                        start "" cmd /c "kubectl port-forward %FRONTEND_POD% 8080:8080"

                        for /f "tokens=*" %%i in ('kubectl get pods -l app=backend -o jsonpath="{.items[0].metadata.name}"') do set BACKEND_POD=%%i
                        echo Backend pod is %BACKEND_POD%
                        start "" cmd /c "kubectl port-forward %BACKEND_POD% 8081:3000"
                    '''
                }
            }
        }

        stage('Parallel Tasks') {
            parallel {
                stage('Run All Tests') {
                    steps {
                        script {
                            bat '''
                                call venv\\Scripts\\activate
                                set PYTHONPATH=%WORKSPACE%
                                echo Running all tests:
                                cd %WORKSPACE%
                                python -m pytest -s -v --tb=short
                            '''
                        }
                    }
                }

                stage('Run Log Analyzer') {
                    steps {
                        script {
                            bat '''
                                call venv\\Scripts\\activate
                                set PYTHONPATH=%WORKSPACE%
                                echo Running log analyzer:
                                cd %WORKSPACE%
                                python scripts\\log_analyzer.py
                            '''
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '**/screenshots/*.png', allowEmptyArchive: true
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
