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
    steps {
      build 'dataproc-test'
    }
  }
  stage('After dataproc-test') {
    steps {
      sh "echo 'Dataproc-test deployed successfully"
    }
  }
}
