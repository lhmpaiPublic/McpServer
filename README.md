이 문서는 **FastAPI 서버를 MySQL, Redis와 함께 Docker로 실행**하고,
**Python 3.12.10 로컬 개발환경**에서도 동일하게 사용할 수 있도록 구성하는 방법을 안내합니다.

---

## 🧱 아키텍처 구성

```
[VS Code + Cursor (LLM Client)]
        │
        │ MCP (HTTP / JSON)
        ▼
[FastAPI MCP Server]   ← Docker / Local
        │
        ├── Redis (Cache)
        └── MySQL (Persistent Data)
```

* LLM(Client)은 **MCP HTTP API**만 호출
* FastAPI는 **Tool Router + 비즈니스 로직 분리**
* Redis는 캐시, MySQL은 영속 데이터 저장소 역할

---

## 🧱 전체 디렉토리 구조

```
project-root/
│
├── docker-compose.yml            # FastAPI + MySQL + Redis
├── Dockerfile                    # FastAPI 실행 이미지
├── Dockerfile_debug              # VS Code 디버그용 이미지
├── requirements.txt              # Python 패키지 목록
├── .env                          # 환경 변수
│
├── .vscode/
│   └── launch.json               # VS Code 디버그 설정
│
└── app/
    ├── main.py                   # FastAPI 엔트리포인트
    │
    ├── mcp/                      # MCP Tool Layer
    │   ├── __init__.py
    │   ├── server.py             # MCP Router (HTTP Endpoint)
    │   └── tools.py              # Tool Logic (DB / Redis)
    │
    ├── db/                       # Infra Layer
    │   ├── __init__.py
    │   ├── mcp_engine.py         # SQLAlchemy Engine (MySQL)
    │   └── redis_client.py       # Redis Client
    │
    ├── static/                   # 정적 리소스
    │   └── assets/
    │
    ├── templates/                # Jinja2 Templates
    │   └── index.html
    │
    └── ai/                       # (확장 예정)
        └── client.py             # LLM Client (Tool Caller)
```

---

## 📌 VS Code 디버그 세팅

다음 파일들은 **디버그 모드 전용**입니다.

* `Dockerfile_debug`
* `docker-compose.yml_debug`

👉 VS Code에서 FastAPI + Docker + breakpoints 디버깅 가능

---

## 📌 1. 실행 방법

⚠ **Windows 환경에서는 Docker Desktop이 실행 중이어야 합니다.**

### 🐳 Docker Compose 실행

```bash
docker-compose up --build
```

### 🚀 백그라운드(데몬) 실행

```bash
docker-compose up --build -d
```

### 🛑 컨테이너 종료

```bash
docker-compose down
```

---

## 🚀 FastAPI 서버 접속

### FastAPI 기본 페이지

* 👉 [http://localhost:8000](http://localhost:8000)

### Swagger UI

* 👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🗄️ MySQL 접속 정보

* **Host**: localhost
* **Port**: 3306

---

## 🔧 Redis 접속 정보

* **Host**: localhost
* **Port**: 6379

---

## 📌 2. 로컬(호스트) Python 3.12.10 가상환경 실행

Docker 컨테이너 외에도
**로컬 Python 3.12.10 환경에서 FastAPI를 직접 실행**할 수 있습니다.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

---

## 📌 3. 구성 완료 항목

이 프로젝트에는 다음 구성 요소가 포함되어 있습니다.

* ✅ FastAPI 개발 서버 (Python 3.12.10)
* ✅ MySQL 8.0.44
* ✅ Redis 7.2
* ✅ Docker 기반 개발 환경
* ✅ `.env` 환경변수 관리
* ✅ DB / Redis 연동 테스트 API
* ✅ MCP Tool 구조 기반 API 설계

---

## 📌 4. `.env` 파일 설정

`.env_backup` 파일을 복사하여 `.env` 파일을 생성합니다.

```env
GIT_PATH=D:/_startupproject/StartupServer
SQL_PATH=D:/psallo/StartupServer/_dbtablesql
CORS_ORIGINS=http://localhost:5173,http://localhost:8000,http://127.0.0.1:8000,http://127.0.0.1:5173
```

---

## 📌 5. MySQL 암호화 관련 설정

MySQL 인증 오류 방지를 위해 아래 패키지를 설치합니다.

```bash
pip install cryptography
```

---

## 📌 6. Docker 캐시 제거 (빌드 오류 시)

```bash
docker build --no-cache -t myfastapi .
```

---

## 📌 7. Docker 캐시 충돌 오류 해결

캐시 충돌로 인해 빌드 오류가 발생할 경우 아래 명령어로 해결할 수 있습니다.

```bash
docker system prune -a
```

⚠ 실행 시 **모든 미사용 Docker 이미지/컨테이너가 제거**됩니다.

---

## ✅ 요약

* Docker / 로컬 환경 **완전 동일 코드**
* MCP 기반 LLM Tool Server 구조
* FastAPI + MySQL + Redis 실무형 구성
* VS Code & Cursor 연동 가능

---

### 🚀 다음 단계 (선택)

* MCP Tool JSON Schema 작성
* LLM Client 자동 Tool 호출
* Tool 체이닝 Agent 구성
* 인증/권한 기반 MCP Server

필요한 항목을 **말해주면 바로 이어서 확장**해 드립니다.
