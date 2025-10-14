pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
                echo 'Compiling Java program...'
                sh 'javac -d bin src/Main.java'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging JAR...'
                sh 'jar cf src\\Main.jar -C src .'
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
            archiveArtifacts artifacts: 'src\\Main.jar', fingerprint: true
        }
    }
}
