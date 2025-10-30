import os
import json
from datasets import load_dataset
from src.NER.utils.util import *
from src.NER.entity.config_entity import *
from src.NER.config.configuration import *

import os
import re
from typing import List, Tuple
from tqdm import tqdm

def read_pubtator_file(file_path: str) -> List[Tuple[str, str]]:
    """
    Converts a PubTator file to token-label pairs.
    Returns a list of sentences, where each sentence = (tokens, labels)
    """
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()

    docs = {}
    current_text = {}
    for line in lines:
        if "|t|" in line or "|a|" in line:
            pmid, part, text = line.strip().split("|", 2)
            docs.setdefault(pmid, {"text": "", "entities": []})
            docs[pmid]["text"] += " " + text
        elif "\t" in line:
            parts = line.strip().split("\t")
            if len(parts) == 5:
                pmid, start, end, entity, etype = parts
                docs[pmid]["entities"].append(
                    (int(start), int(end), entity, etype)
                )

    sentences = []
    for pmid, doc in tqdm(docs.items(), desc=f"Parsing {os.path.basename(file_path)}"):
        text = doc["text"]
        labels = ["O"] * len(text)

        for start, end, entity, etype in doc["entities"]:
            labels[start] = f"B-{etype}"
            for i in range(start + 1, end):
                labels[i] = f"I-{etype}"

        # Simple whitespace tokenization
        tokens = []
        token_labels = []
        for match in re.finditer(r"\S+", text):
            token = match.group()
            start = match.start()
            label = labels[start] if start < len(labels) else "O"
            tokens.append(token)
            token_labels.append(label)

        sentences.append((tokens, token_labels))

    return sentences


def write_tsv(sentences: List[Tuple[List[str], List[str]]], out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        for tokens, labels in sentences:
            for t, l in zip(tokens, labels):
                f.write(f"{t}\t{l}\n")
            f.write("\n")
    print(f"✅ Saved {out_path} ({len(sentences)} sentences)")


def prepare_bc5cdr_dataset(raw_dir: str, out_dir: str):
    mapping = {
        "CDR_TrainingSet.PubTator.txt": "train.tsv",
        "CDR_DevelopmentSet.PubTator.txt": "dev.tsv",
        "CDR_TestSet.PubTator.txt": "test.tsv",
    }

    for fname, outname in mapping.items():
        fpath = os.path.join(raw_dir, "CDR.Corpus.v010516", fname)
        print(f"raw_dir {raw_dir}")
        if not os.path.exists(fpath):
            print(f"⚠️ Missing {fname}, skipping.")
            continue

        sentences = read_pubtator_file(fpath)
        write_tsv(sentences, os.path.join(out_dir, outname))


if __name__ == "__main__":
    RAW_DIR = "data/BC5CDR"
    OUT_DIR = "data/bc5cdr_prepared"
    prepare_bc5cdr_dataset(RAW_DIR, OUT_DIR)
    print("🎯 BC5CDR dataset prepared successfully!")



