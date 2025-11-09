import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer
import os

class NERDataset(Dataset):
    def __init__(self, filepath, label2id, tokenizer_name, max_length=128):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.max_length = max_length
        self.label2id = label2id
        self.sentences, self.labels = self.load_tsv(filepath)

    def load_tsv(self, filepath):
        sentences, labels = [], []
        tokens, tags = [], []
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                if line.strip() == "":
                    if tokens:
                        sentences.append(tokens)
                        labels.append(tags)
                        tokens, tags = [], []
                else:
                    token, tag = line.strip().split("\t")
                    tokens.append(token)
                    tags.append(tag)
        return sentences, labels

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, idx):
        tokens = self.sentences[idx]
        labels = self.labels[idx]

        encoding = self.tokenizer(
            tokens,
            is_split_into_words=True,
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        )

        label_ids = [self.label2id.get(l, self.label2id["O"]) for l in labels]
        label_ids = label_ids[:self.max_length] + [self.label2id["O"]] * (self.max_length - len(label_ids))
        encoding["labels"] = torch.tensor(label_ids)
        return {k: v.squeeze(0) for k, v in encoding.items()}


def build_label_map(tsv_file):
    labels = set()
    with open(tsv_file, encoding="utf-8") as f:
        for line in f:
            if line.strip() == "":
                continue
            _, tag = line.strip().split("\t")
            labels.add(tag)
    label2id = {label: idx for idx, label in enumerate(sorted(labels))}
    id2label = {v: k for k, v in label2id.items()}
    return label2id, id2label
