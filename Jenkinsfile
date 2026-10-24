pipeline {
    agent any
    // 코드 푸시(웹훅) 및 1분 주기 자동 실행 설정
    triggers {
        githubPush()        // GitHub 웹훅 트리거 유지 (GitHub hook trigger for GITScm polling)
        cron('H/1 * * * *') // 무조건 1분마다 실행 (Build periodically)
        // cron('''TZ=Asia/Seoul H 2 * * *''')
    }

    stages {
        stage('1. 코드 확인') {
            steps {
                echo '⏰ 파이프라인이 실행되었습니다! 현재 시각 및 파일 목록을 확인합니다.'
                sh 'date'
                sh 'ls -la'
            }
        }
        stage('2. Docker 이미지 빌드 (CI)') {
            steps {
                echo '=== 애플리케이션 Docker 이미지를 빌드합니다 ==='
                sh 'docker build -f Dockerfile.app -t my-web-app:latest .'
            }
        }
        stage('3. 컨테이너 배포 (CD)') {
            steps {
                echo '=== 기존 컨테이너를 중지하고 새 버전을 배포합니다 ==='
                // 기존에 실행 중인 컨테이너가 있다면 삭제 (없어도 에러 무시하도록 || true 추가)
                sh 'docker rm -f my-running-app || true'
                // 새 이미지를 8000번 포트로 백그라운드 실행
                sh 'docker run -d --name my-running-app -p 8000:8000 my-web-app:latest'
            }
        }
    }
}