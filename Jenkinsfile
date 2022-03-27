pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building docker image..'
                bat 'docker build -t galicia-landing .'
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}