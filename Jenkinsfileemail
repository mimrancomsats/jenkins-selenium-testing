
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('selenium-project') {
                    sh '''
                        python3 -m venv selenium-env
                        . selenium-env/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                dir('selenium-project') {
                    sh '''
                        . selenium-env/bin/activate
                        mkdir -p reports
                        pytest -v --junitxml=reports/results.xml test-suite/
                    '''
                }
            }
        }
    }

    post {
        always {
            dir('selenium-project') {
                junit allowEmptyResults: true,
                      testResults: 'reports/results.xml'

                emailext(
                    to: 'imrantaurus2003@gmail.com',
                    subject: "Selenium Test Results: ${currentBuild.currentResult} - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
Hello QA Team,

The Selenium test execution has completed.

Build Status: ${currentBuild.currentResult}
Project: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}

Please visit the following link to view the build details and test results:

${env.BUILD_URL}

Regards,
Jenkins CI/CD Pipeline
"""
                )
            }
        }
    }
}
