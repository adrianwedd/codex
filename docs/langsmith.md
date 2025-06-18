# LangChain and LangSmith

Codex CLI can use the LangChain provider and record traces to [LangSmith](https://smith.langchain.com/).

## Configuration

Add the `langchain` provider to your `~/.codex/config.json` if it is not already present:

```json
{
  "providers": {
    "langchain": {
      "name": "LangChain",
      "baseURL": "http://localhost:8000",
      "envKey": "LANGCHAIN_API_KEY"
    }
  }
}
```

Set the following environment variables (in `.env` or `~/.codex.env`) to enable tracing:

```bash
export LANGCHAIN_API_KEY="your-langsmith-key"
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
```

## Example scripts

See [codex-cli/examples/langchain](../codex-cli/examples/langchain) for small Python examples that use LangChain. When the variables above are set, interactions will appear in your LangSmith dashboard.
