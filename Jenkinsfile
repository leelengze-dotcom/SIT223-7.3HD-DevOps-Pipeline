pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code retrieved from GitHub'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'python3 -m pytest -v'
            }
        }
        stage('Code Quality') {
            steps {
                echo 'Running code quality analysis...'
                sh 'python3 -m pylint app.py --fail-under=7.0'
            }
        }
        stage('Security') {
            steps {
                echo 'Running security analysis...'
                sh 'python3 -m bandit -r app.py'
            }
        }
    }
}
