pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/meyudha/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Bandit') {
            steps {
                sh 'pip install bandit'
            }
        }

        stage('Run Bandit (SAST Analysis)') {
            steps {
                sh 'bandit -f xml -o bandit-output.xml -r . || true'
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
