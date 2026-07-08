import { useState } from 'react'
import { generatePrompt } from './api/llm'
import type { LLMResponse } from './types'

function App() {
  const [prompt, setPrompt] = useState('')
  const [response, setResponse] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setError('')
    setResponse('')

    if (!prompt.trim()) {
      setError('Please enter a prompt.')
      return
    }

    setLoading(true)
    try {
      const result: LLMResponse = await generatePrompt(prompt)
      setResponse(result.response)
    } catch (err) {
      setError((err as Error).message || 'Failed to fetch response.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-shell">
      <header>
        <h1>Self LLM Starter</h1>
        <p>A minimal local LLM UI connected to a FastAPI backend.</p>
      </header>

      <main>
        <form onSubmit={handleSubmit} className="prompt-form">
          <label htmlFor="prompt">Prompt</label>
          <textarea
            id="prompt"
            rows={6}
            value={prompt}
            onChange={(event) => setPrompt(event.target.value)}
            placeholder="Ask your local model a question..."
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Generating…' : 'Generate'}
          </button>
        </form>

        {error && <div className="notice error">{error}</div>}
        {response && (
          <section className="response-block">
            <h2>Response</h2>
            <pre>{response}</pre>
          </section>
        )}
      </main>
    </div>
  )
}

export default App
