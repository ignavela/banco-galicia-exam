pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                docker --version
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