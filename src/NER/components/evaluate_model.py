import os
import json
import sys
import numpy as np
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    Trainer,
    TrainingArguments
)
from seqeval.metrics import classification_report, f1_score
from src.NER.exception import NerException
from src.NER.logger.logging import logging


def load_conll_tsv(path):
    sentences, labels = [], []
    tokens, tags = [], []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                if tokens:
                    sentences.append(tokens)
                    labels.append(tags)
                    tokens, tags = [], []
            else:
                token, tag = line.split("\t")
                tokens.append(token)
                tags.append(tag)

    if tokens:
        sentences.append(tokens)
        labels.append(tags)

    return Dataset.from_dict({
        "tokens": sentences,
        "ner_tags": labels
    })


def tokenize_and_align_labels(examples, tokenizer, label2id):
    tokenized = tokenizer(
        examples["tokens"],
        is_split_into_words=True,
        truncation=True,
        padding="max_length",
        max_length=128
    )

    aligned_labels = []
    for i in range(len(examples["tokens"])):
        word_ids = tokenized.word_ids(batch_index=i)
        label_ids = []
        prev_word_idx = None

        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != prev_word_idx:
                label_ids.append(label2id[examples["ner_tags"][i][word_idx]])
            else:
                label_ids.append(label2id[examples["ner_tags"][i][word_idx]])

            prev_word_idx = word_idx

        aligned_labels.append(label_ids)

    tokenized["labels"] = aligned_labels
    return tokenized


def evaluate_model(model_path: str, test_tsv: str):
    try:
        logging.info(f"Loading model from: {model_path}")

        tokenizer = AutoTokenizer.from_pretrained(
            "dmis-lab/biobert-base-cased-v1.1"
        )
        model = AutoModelForTokenClassification.from_pretrained(model_path)

        label2id = model.config.label2id
        id2label = model.config.id2label

        logging.info(f"Loading dataset from: {test_tsv}")
        dataset = load_conll_tsv(test_tsv)

        dataset = dataset.map(
            tokenize_and_align_labels,
            batched=True,
            fn_kwargs={
                "tokenizer": tokenizer,
                "label2id": label2id
            }
        )

        dataset.set_format(
            type="torch",
            columns=["input_ids", "attention_mask", "labels"]
        )

        trainer = Trainer(
            model=model,
            args=TrainingArguments(
                output_dir="Artifacts/eval",
                per_device_eval_batch_size=8,
                remove_unused_columns=False
            )
        )

        logging.info("Running evaluation...")
        predictions, labels, _ = trainer.predict(dataset)
        predictions = np.argmax(predictions, axis=2)

        true_labels = []
        pred_labels = []

        for pred, label in zip(predictions, labels):
            t, p = [], []
            for pr, lb in zip(pred, label):
                if lb != -100:
                    t.append(id2label[lb])
                    p.append(id2label[pr])
            true_labels.append(t)
            pred_labels.append(p)

        print("\n Classification Report")
        print(classification_report(true_labels, pred_labels))

        f1 = f1_score(true_labels, pred_labels)
        print(f"\n F1 Score: {f1:.4f}")

        with open("Artifacts/eval/eval_metrics.json", "w") as f:
            json.dump({"f1": f1}, f, indent=4)

        logging.info("Evaluation completed successfully.")

    except Exception as e:
        raise NerException(e, sys)




























# import os,sys
# import json
# import torch
# import matplotlib.pyplot as plt
# import seaborn as sns
# from datasets import load_dataset
# from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer
# from seqeval.metrics import (
#     classification_report,
#     f1_score,
#     precision_score,
#     recall_score
# )
# from sklearn.metrics import confusion_matrix
# import numpy as np
# from src.NER.utils.util import create_directories
# from src.NER.exception import *


# def evaluate_model(model_path, dataset_path, output_dir="Artifacts/result") :
#     create_directories([output_dir])
#     try :
#         logger.info(f"loading model form: {model_path}")
#         #tokenizer = AutoTokenizer.from_pretrained(model_path)
#         tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
#         model = AutoModelForTokenClassification.from_pretrained(model_path)
#         logger.info(f"loading dataset form: {dataset_path}")
#         dataset = load_dataset("csv",data_files={"text":dataset_path}, delimiter = "\t")["text"]
#     except Exception as e :
#         raise NerException(e,sys) from e
    
#     # --- Tokenization step --- 
#     def tokenize_and_align_labels(examples) :
#         tokenized_input = tokenizer(
#             examples["tokens"],
#             truncation = True,
#             is_split_into_words = True,
#             padding = "max_length",
#             max_length = 128
#         )
#         tokenized_input["labels"] = examples["labels"]
#         return tokenized_input
    
#     # NOTE: Ensure dataset has "tokens" and labels columns before this step.
#     # For TSV, adjust yourt data loading logic accordingly

#     trainer = Trainer(model=model)
#     logger.info("Running evaluation.......")

#     predictions, labels, _ = trainer.predict(dataset)
#     predictions = np.argmax(predictions, axis = 2)
    

#     id2label = model.config.id2label
#     true_labels = [[id2label.get(int(l), "O") for l in label if l != -100] for label in labels]
#     pred_labels = [[id2label.get(int(p), "O") for (p, l) in zip(pred, label) if l != -100] for pred, label in zip(predictions, labels)]

#     # --- Compute core metrics ---
#     metrics = {
#         "precision": precision_score(true_labels, pred_labels),
#         "recall": recall_score(true_labels, pred_labels),
#         "f1": f1_score(true_labels, pred_labels)
#     }

#     logger.info("\n=== Classification Report ===")
#     logger.info(classification_report(true_labels, pred_labels))
#     logger.info("\n=== Summary Metrics ===")
#     logger.info(json.dumps(metrics, index = 4))
#     print(json.dumps(metrics, indent=4))

#     # Save Metrics

#     with open(os.path.join(output_dir, "eval_metrics.json"), "w") as f:
#         json.dump(metrics, f, indent=4)
    
#     print(f"metrics save to {output_dir}/eval_metrics.json")

#     print("\n Generating per-entity F1 visualization.....")
#     report_dict = classification_report(true_labels, pred_labels, output_dir=True)
#     entity_labels = [k for k in report_dict.keys() if k not in ["micro avg", "macro avg", "weighted avg", "accuracy"]]
#     #entity_f1 = [report_dict[k]]
#     print(f"Report Derectories {report_dict}")