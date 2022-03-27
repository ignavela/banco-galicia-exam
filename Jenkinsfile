pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                checkout scm
                bat 'docker --version'
                bat 'docker build -t galicia-landing .'
                echo 'Building..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}