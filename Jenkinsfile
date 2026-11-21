
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

                        # Create reports directory
                        mkdir -p reports

                        # Execute pytest
                        pytest -v --junitxml=reports/results.xml tests/
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
            }
        }
    }
}
