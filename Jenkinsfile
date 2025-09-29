pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
                echo 'Compiling Java program...'
                sh 'javac src/Main.java'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Java program...'
                sh 'java -cp src Main'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'out/*.class', fingerprint: true
        }
    }
}
