from app.clients.ollama_client import OllamaClient
from app.core.config import settings

client = OllamaClient(base_url=settings.local_llm_url)


def generate_text(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("Prompt must not be empty.")

    response = client.send_prompt(prompt, model=settings.default_model)
    return response
