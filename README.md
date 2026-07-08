# Self LLM

A minimal starter project for a local LLM application.

This repository contains a Python FastAPI backend and a React + Vite + TypeScript frontend. It is designed as a local-first skeleton for connecting to a local LLM service without cloud API dependencies.

## 프로젝트 구조

```
self-llm/
├── backend/
│   ├── .env.example
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   └── llm.py
│   │   │   └── router.py
│   │   ├── clients/
│   │   │   └── ollama_client.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── models/
│   │   │   └── llm_model.py
│   │   ├── schemas/
│   │   │   └── llm.py
│   │   ├── services/
│   │   │   └── llm_service.py
│   │   └── main.py
│   ├── pyproject.toml
│   ├── README.md
│   └── requirements.txt
├── frontend/
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── README.md
│   └── src/
│       ├── api/
│       │   └── llm.ts
│       ├── components/
│       ├── types/
│       │   └── index.ts
│       ├── App.tsx
│       ├── index.css
│       └── main.tsx
├── .gitignore
└── LICENSE
```

## 주요 기능

- FastAPI 백엔드 기본 스켈레톤
- React + Vite + TypeScript 프론트엔드
- 로컬 LLM 호출 포인트 예시 (Ollama 스타일 요청)
- 기본적인 에러 처리 및 구조화된 모듈 구성
- 로컬 개발 환경에서 즉시 실행 가능한 형태

## 설치 및 실행

### 1. 백엔드 실행

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

백엔드는 `http://localhost:8000`에서 실행됩니다.

### 2. 프론트엔드 실행

```bash
cd frontend
npm install
npm run dev
```

프론트엔드는 기본적으로 `http://localhost:4173`에서 실행됩니다.

### 3. 로컬 LLM 연결 포인트 설정

`backend/.env.example` 파일을 참고하여 `.env` 파일을 생성하세요. 기본값은 다음과 같습니다.

```ini
ENVIRONMENT=development
LOCAL_LLM_URL=http://localhost:11434
DEFAULT_MODEL=local-llm
```

로컬 LLM 서버가 `http://localhost:11434`에서 실행 중이어야 하며, Ollama 호환 HTTP API를 사용하는 경우 자동으로 연결 포인트가 동작하도록 구성되어 있습니다.

## API 엔드포인트

- `GET /health`
  - 상태 확인용 엔드포인트
- `POST /api/llm/generate`
  - 요청 본문 예시: `{ "prompt": "Hello local LLM" }`

### 요청 예시

```bash
curl -X POST http://localhost:8000/api/llm/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello local LLM"}'
```

## 개발 가이드

- `backend/app/clients/ollama_client.py`는 로컬 LLM 호출을 담당합니다.
- `backend/app/services/llm_service.py`는 프롬프트 유효성 검사와 요청 흐름을 관리합니다.
- `backend/app/api/endpoints/llm.py`는 외부 요청을 처리하는 FastAPI 라우터입니다.
- `frontend/src/api/llm.ts`는 백엔드 API 호출 기능을 제공합니다.
- `frontend/src/App.tsx`는 사용자 입력과 결과 표시 UI를 담당합니다.

## 주요 명령어

- `cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- `cd frontend && npm install`
- `cd frontend && npm run dev`

## 참고

이 프로젝트는 로컬 LLM 기반 애플리케이션을 빠르게 시작할 수 있는 최소 기능 스켈레톤입니다. 모델 다운로드나 실제 LLM 실행 로직은 포함하지 않으며, 로컬 LLM 서버와 연결할 수 있는 구현 포인트를 제공합니다.
