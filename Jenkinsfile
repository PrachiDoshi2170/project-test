node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Trigger dataproc-test') {
    build 'dataproc-test'
  }
  stage('After dataproc-test') {
    sh "echo 'Dataproc-test deployed successfully"
  }
}
