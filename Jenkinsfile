pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker --version'
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