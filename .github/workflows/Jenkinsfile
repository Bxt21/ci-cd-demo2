pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/ci-cd-demo2.git'  // Replace with your GitHub username
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'  // Install dependencies
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'  // Run tests using pytest
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application locally...'
                sh 'python app.py'  // Run the app locally
            }
        }
    }
}
