pipeline {
  agent any
  stages {
      stage("Stage 1") {
          steps {
              sh """
              #!/bin/bash
              ls -la ./
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