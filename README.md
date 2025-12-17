이 문서는 FastAPI 서버를 MySQL, Redis와 함께 Docker로 실행하고  
Python 3.12.10 로컬 개발환경에서도 사용할 수 있도록 구성하는 방법을 안내합니다.


---
[VS Code + Cursor (LLM Client)]
        │
        │ MCP (HTTP)
        ▼
[FastAPI MCP Server]  ← Docker
        │
        ├── Redis (cache)
        └── MySQL (data)


## 📌 vccode debuge 세팅에 대해서

✅ Dockerfile_debug, docker-compose.yml_debug - 디버그로 사용되는 파일입니다.

## 📌 1. 실행 방법

📌 윈도우 환경이면 Docker Desktop이 실행 되어있어야 한다.

### 🐳 Docker Compose 실행

```bash
docker-compose up --build
🚀 demon 실행
docker-compose up --build -d
docker-compose down
🚀 FastAPI 서버 접속

FastAPI:
👉 http://localhost:8000

Swagger UI:
👉 http://localhost:8000/docs

🗄️ MySQL 접속 정보

Host: localhost

Port: 3306

🔧 Redis 접속 정보

Host: localhost

Port: 6379

📌 2. 로컬(호스트) Python 3.12.10 가상환경

Docker 컨테이너 외에도 로컬 환경에서 직접 FastAPI 실행이 가능합니다.

📌 3. 구성 완료

이 프로젝트에는 아래 요소가 포함됩니다:

✅ FastAPI 개발 서버 (Python 3.12.10)

✅ MySQL 8.0.44

✅ Redis 7.2

✅ Docker 기반 개발 환경

✅ .env 환경변수 관리

✅ DB 및 Redis 연결 테스트 API 포함

📌 4. env 파일 설정

✅ .env_backup 을 복사해서 .env파일로 만든다.

✅ 프로젝트 폴더경로 세팅 : GIT_PATH=D:/_startupproject/StartupServer

✅ sql파일 mysql import 할 파일 경로 : SQL_PATH=D:/psallo/StartupServer/_dbtablesql

✅ CORS 에러 URL 등록 : CORS_ORIGINS=http://localhost:5173,http://localhost:8000,http://127.0.0.1:8000,http://127.0.0.1:5173


📌 5. mysql
🚀 mysql 암호화 그냥 입력으로 쓰겠다 패키지 설치 : cryptography

📌 6. docker cache 제거
 docker build --no-cache -t myfastapi .

📌 7. 캐쉬에러
![캐시 에러 화면]("./images_readme/error1_image.png")


```
