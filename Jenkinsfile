pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'github-credentials-id'
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: env.GITHUB_CREDENTIALS, url: 'https://github.com/dipyomoybarua/python-locust-api-poc.git'
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
                    '''
                }
            }
        }
        stage('Run Tests in Parallel') {
            steps {
                script {
                    def parallelism = 4

                    bat """
                        call venv\\Scripts\\activate
                        set PYTHONPATH=%WORKSPACE%
                        pytest -n ${parallelism}
                    """
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