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
                bat 'pip install bandit'
            }
        }

        stage('Run Bandit (SAST Analysis)') {
            steps {
                bat 'bandit -f xml -o bandit-output.xml -r . || exit 0'
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
