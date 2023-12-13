pipeline {
  agent any
  stages {
      stage("Stage 1") {
          steps {
              sh """
              #!/bin/bash
              echo "Hello from pipeline"
              """
          }
      }
      stage("Stage 2") {
          steps {
              sh """
              #!/bin/bash
              echo "Hello from pipeline"
              exit 1
              """
          }
      }
  }
}