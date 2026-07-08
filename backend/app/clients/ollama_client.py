from typing import Dict
import httpx


class OllamaClient:
    """Minimal local LLM client stub for Ollama-style HTTP endpoints."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def send_prompt(self, prompt: str, model: str = "local-llm") -> str:
        url = f"{self.base_url}/v1/generate"
        payload: Dict[str, object] = {
            "model": model,
            "prompt": prompt,
            "max_tokens": 300,
        }
        try:
            with httpx.Client(timeout=10.0) as client:
                resp = client.post(url, json=payload)
                resp.raise_for_status()
                data = resp.json()
                return data.get("output", "") or data.get("response", "") or ""
        except httpx.RequestError as exc:
            raise RuntimeError(f"Local LLM request failed: {exc}") from exc
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(f"Local LLM returned {exc.response.status_code}: {exc.response.text}") from exc
