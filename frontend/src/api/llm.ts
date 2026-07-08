import type { LLMRequest, LLMResponse } from '../types'

const API_BASE = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000/api'

export async function generatePrompt(prompt: string): Promise<LLMResponse> {
  const requestBody: LLMRequest = { prompt }

  const response = await fetch(`${API_BASE}/llm/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(requestBody),
  })

  if (!response.ok) {
    const errorPayload = await response.json().catch(() => null)
    const detail = errorPayload?.detail || response.statusText
    throw new Error(`Backend error: ${detail}`)
  }

  return response.json()
}
