pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vinodkumarjayantha/FlaskDemo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --html=reports/report.html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html'
            }
        }
    }
}