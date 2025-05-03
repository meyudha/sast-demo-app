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
                bat '"C:\\Users\\meyudha\\AppData\\Roaming\\Python\\Python38\\Scripts\\pip.exe" install bandit'
            }
        }
        stage('SAST Analysis') {
            steps {
                bat '"C:\\Users\\meyudha\\AppData\\Roaming\\Python\\Python38\\Scripts\\bandit.exe" -f xml -o bandit-output.xml -r . || exit 0'
                recordIssues tools: [pythonBandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}

