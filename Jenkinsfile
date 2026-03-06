pipeline {
    agent any
    stages {
        stage ('clone Repository') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        stage ('Build Docker Image') {
            steps {
                sh 'docker build -t my-flask-demo .'
            }
        }
        stage ('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 my-flask-demo'
            }
        }
    }
    
}