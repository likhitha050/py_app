pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerID')
    IMAGE_NAME = "cslikhitha/py_app"
  }

  stages {
    stage('Checkout') {
      steps {
        git(
          url: 'https://github.com/likhitha050/py_app.git',
          branch: 'main',
          credentialsId: 'dockerID'
        )
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_NAME}:latest")
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry('https://index.docker.io/v1/', 'dockerID') {
            dockerImage.push()
          }
        }
      }
    }
  }

  post {
    always {
      echo "Cleaning up workspace..."
      deleteDir()
    }
    success {
      echo 'Pipeline succeeded!'
    }
    failure {
      echo 'Pipeline failed!'
    }
  }
}
