from pydantic import BaseSettings

class Settings(BaseSettings):
    environment: str = "development"
    local_llm_url: str = "http://localhost:11434"  # Example local LLM proxy endpoint
    default_model: str = "local-llm"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
