pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker --version'
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