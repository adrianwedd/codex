"""Prompt clustering with LangChain embeddings.

This is a simplified variant of ``cluster_prompts.py`` that uses LangChain's
``OpenAIEmbeddings`` helper. Provide a CSV file with a ``prompt`` column.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def load_prompts(path: Path) -> pd.Series:
    df = pd.read_csv(path)
    if "prompt" not in df.columns:
        raise SystemExit("CSV must contain a 'prompt' column")
    return df["prompt"]


def embed_prompts(prompts: pd.Series) -> list[list[float]]:
    embed = OpenAIEmbeddings()
    return [embed.embed_query(p) for p in prompts.tolist()]


def cluster(vectors: list[list[float]], k_max: int = 10) -> list[int]:
    best_k = 2
    best_score = -1.0
    best_labels: list[int] | None = None
    for k in range(2, k_max + 1):
        km = KMeans(n_clusters=k, n_init="auto", random_state=42)
        labels = km.fit_predict(vectors)
        try:
            score = silhouette_score(vectors, labels)
        except ValueError:
            continue
        if score > best_score:
            best_k = k
            best_score = score
            best_labels = labels
    if best_labels is None:
        raise RuntimeError("Failed to find a suitable k")
    print(f"Selected k={best_k} (silhouette={best_score:.3f})")
    return best_labels.tolist()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, default=Path("prompts.csv"))
    args = ap.parse_args()

    prompts = load_prompts(args.csv)
    vectors = embed_prompts(prompts)
    labels = cluster(vectors)
    out = pd.DataFrame({"prompt": prompts, "cluster": labels})
    out.to_csv("clusters.csv", index=False)
    print("Written clusters.csv")


if __name__ == "__main__":
    main()

