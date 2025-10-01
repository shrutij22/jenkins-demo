pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
                echo 'Compiling Java program...'
                bat 'javac -d src src\\Main.java'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging JAR...'
                bat 'jar cf src\\Main.jar -C src .'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Java program...'
                bat 'java -cp src Main'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'src\\Main.jar', fingerprint: true
        }
    }
}
