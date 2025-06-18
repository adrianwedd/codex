"""Minimal RAG pipeline using LangChain and LangSmith.

Load documents from a folder, build a FAISS vector store and answer a question.

Example usage:
    python rag_pipeline.py docs "What is codex?"
"""
from __future__ import annotations
import argparse
from pathlib import Path

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA


def load_docs(path: Path) -> list[Document]:
    texts: list[Document] = []
    for p in path.rglob("*.txt"):
        txt = p.read_text()
        texts.append(Document(page_content=txt, metadata={"source": str(p)}))
    return texts


def build_vector_store(docs: list[Document]):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=50
    )
    split = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(split, embeddings)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docs", type=Path)
    parser.add_argument("question")
    args = parser.parse_args()

    docs = load_docs(args.docs)
    store = build_vector_store(docs)
    retriever = store.as_retriever()
    llm = ChatOpenAI()
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    print(chain.invoke({"query": args.question}))


if __name__ == "__main__":
    main()

