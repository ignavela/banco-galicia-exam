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
                echo 'Stopping docker container..'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat 'docker stop galicia-container'
                }
                echo 'Deploying docker container..'
                bat 'docker run -p 8082:80 --name galicia-container galicia-landing'            
            }
        }
    }
}