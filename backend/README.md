# backend

FastAPI backend for the local LLM starter.

## 실행

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn[standard] pydantic python-dotenv httpx
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 엔드포인트

- `GET /health`
- `POST /api/llm/generate`

## 로컬 LLM 구성

`.env` 또는 `.env.example`을 사용하여 `LOCAL_LLM_URL`을 설정하세요.
