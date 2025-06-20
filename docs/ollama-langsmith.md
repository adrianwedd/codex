# Ollama with LangSmith tracing

This example shows how to configure Codex CLI to use a local model served by [Ollama](https://ollama.ai) while capturing requests in your LangSmith dashboard.

Save the configuration below as `~/.codex/config.json` (also available at
`docs/example-configs/ollama-langsmith.json`):

```json
{
  "model": "mistral",
  "provider": "ollama",
  "providers": {
    "ollama": {
      "name": "Ollama",
      "baseURL": "http://localhost:11434/v1"
    }
  }
}
```

Then create an `.env` file (or `~/.codex.env`) with the following variables
(see `docs/example-configs/ollama-langsmith.env`):

```bash
# LangSmith tracing
LANGCHAIN_API_KEY="your-langsmith-key"
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
```

When these environment variables are present, Codex CLI will wrap OpenAI calls with LangSmith tracing so interactions appear on your LangSmith account.

## Quick launch script

For convenience, a helper script checks for all required tools and variables before starting Codex with this configuration:

```bash
scripts/launch_ollama_langsmith.sh "your prompt here"
```

The script verifies the Ollama server, loads the environment variables from `docs/example-configs/ollama-langsmith.env` if present, and then launches the Codex CLI using the example configuration.
