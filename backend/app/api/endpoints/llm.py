from fastapi import APIRouter, HTTPException
from app.schemas import llm as llm_schema
from app.services import llm_service

router = APIRouter()

@router.post("/generate", response_model=llm_schema.LLMResponse)
async def generate_text(request: llm_schema.LLMRequest):
    try:
        result = llm_service.generate_text(request.prompt)
        return llm_schema.LLMResponse(
            prompt=request.prompt,
            response=result,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
