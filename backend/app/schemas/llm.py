from pydantic import BaseModel

class LLMRequest(BaseModel):
    prompt: str

class LLMResponse(BaseModel):
    prompt: str
    response: str
