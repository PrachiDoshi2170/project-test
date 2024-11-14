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
  post {
    success {
      // Trigger the second pipeline
      build job: 'Fetch-GCloud-Version-Pipeline'
    }
    failure {
      echo 'Pipeline failed. Skipping downstream job trigger.'
    }
  }
}
