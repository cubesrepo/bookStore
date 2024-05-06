pipeline{
    agent any
    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/bookStore'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv bookStoreVENV'
                bat 'bookStoreVENV\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'bookStoreVENV\\Scripts\\activate && pytest -v --html=report.html --headless'
            }
        }
    }
}