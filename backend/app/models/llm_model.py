from dataclasses import dataclass


@dataclass
class LLMModelConfig:
    name: str
    description: str
    max_tokens: int = 300
