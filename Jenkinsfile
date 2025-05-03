pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/meyudha/sast-demo-app.git'
            }
        }

        stage('Install Bandit') {
            steps {
                bat 'pip install bandit'
            }
        }

        stage('Run Bandit (SAST Analysis)') {
            steps {
                bat 'bandit -f xml -o bandit-output.xml -r . || exit 0'
            }
        }

        stage('Record Bandit Warnings') {
            steps {
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
