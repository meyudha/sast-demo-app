pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/meyudha/sast-demo-app.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install bandit'
            }
        }
        stage('SAST Analysis') {
            steps {
                bat 'bandit -f xml -o bandit-output.xml -r . || exit 0'
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}

