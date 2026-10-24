pipeline {
    agent any

    stages {
        stage('1. 코드 클론 확인') {
            steps {
                echo '=== GitHub에서 가져온 파일 목록 확인 ==='
                sh 'pwd'
                sh 'ls -la'
            }
        }
        stage('2. 애플리케이션 실행 및 테스트') {
            steps {
                echo '=== Python 스크립트 실행 ==='
                sh 'python3 app.py'
            }
        }
    }
    post {
        success {
            echo '🎉 GitHub 연동 빌드가 성공적으로 완료되었습니다!'
        }
        failure {
            echo '❌ 빌드 중 에러가 발생했습니다.'
        }
    }
}