pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
                echo 'Compiling Java program...'
                sh 'javac Main.java'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Java program...'
                sh 'java Main'
            }
        }
    }
}
