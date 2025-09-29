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
            // Archive the compiled class files or JAR here
            // Since you don't have a JAR, let's archive the compiled class files in src folder
            archiveArtifacts artifacts: 'src/*.class', fingerprint: true
        }
