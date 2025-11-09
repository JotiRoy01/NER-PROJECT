from transformers import AutoModelForTokenClassification, Trainer, TrainingArguments
from src.NER.components.dataset_builder import NERDataset, build_label_map
from src.NER.entity.config_entity import Artifact, DataLoaderArtifacts, Dataset_dir, Model_name, Training
from src.NER.exception import NerException
from src.NER.logger.logging import logging
import os



def train_bc5cdr(modelname:Model_name, dataset_dir:Dataset_dir, train_info:Training) :
    label2id, id2label = build_label_map(dataset_dir.train_path_tsv)
    model = AutoModelForTokenClassification.from_pretrained(
        modelname.model_name,
        num_labels = len(label2id),
        id2label = id2label,
        label2id = label2id
    )

    train_dataset = NERDataset(
        dataset_dir.train_path_tsv,
        label2id,
        modelname.model_name,
        dataset_dir.max_lenght
    )
    dev_dataset = NERDataset(
        dataset_dir.dev_path_tsv,
        label2id,
        modelname.model_name,
        dataset_dir.max_lenght
    )

    args = TrainingArguments(
        train_info.output_dir,
        eval_strategy = "steps",
        save_strategy="epoch",
        learning_rate= float(train_info.learning_rate),
        per_device_train_batch_size= train_info.batch_size,
        per_device_eval_batch_size=train_info.batch_size,
        num_train_epochs=train_info.epochs,
        logging_steps=train_info.logging_steps,
        report_to="none"

    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset= dev_dataset,
        tokenizer = train_dataset.tokenizer
    )

    trainer.train()
    model.save_pretrained(train_info.output_dir)
    print(f"model saved to {train_info.output_dir}")