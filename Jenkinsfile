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
                echo 'Stopping and deleting docker container..'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat 'docker stop galicia-container'
                    bat 'docker rm galicia-container'
                }
                echo 'Deploying docker container..'
                bat 'docker run -d -p 8082:80 --name galicia-container galicia-landing' 
            }
        }
    }
}