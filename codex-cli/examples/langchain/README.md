# LangChain examples

This folder contains small examples that use the [LangChain](https://github.com/hwchase17/langchain) library together with Codex CLI.

Tracing can be enabled by setting the `LANGCHAIN_TRACING_V2` and `LANGCHAIN_ENDPOINT` environment variables (along with your `LANGCHAIN_API_KEY`). These variables may be placed in `.env` or `~/.codex.env` so they are loaded automatically.

Run `pip install langchain langsmith openai faiss-cpu` to install the required packages.

* `rag_pipeline.py` – minimal retrieval‑augmented generation demo.
* `cluster_prompts_langchain.py` – clusters prompts with embeddings and LangSmith tracing.
