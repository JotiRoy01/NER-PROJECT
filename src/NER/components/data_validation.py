import os
from typing import List, Tuple

class DataValidationError(Exception):
    """Custom exception for dataset validation errors."""
    pass


class NERDataValidator:
    def __init__(self, valid_labels: List[str] = None):
        self.valid_labels = set(valid_labels) if valid_labels else None

    def validate_tsv_file(self, file_path: str):
        if not os.path.exists(file_path):
            raise DataValidationError(f" Missing file: {file_path}")

        sentences, errors = 0, 0
        tokens, tags = [], []

        with open(file_path, encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    if tokens:
                        sentences += 1
                        tokens, tags = [], []
                    continue

                parts = line.split("\t")
                if len(parts) != 2:
                    print(f" Malformed line {i}: {line}")
                    errors += 1
                    continue

                token, label = parts
                if not token or not label:
                    print(f" Empty token/label at line {i}")
                    errors += 1
                    continue

                if self.valid_labels and label not in self.valid_labels:
                    print(f" Unknown label '{label}' at line {i}")
                    errors += 1
                    continue

                tokens.append(token)
                tags.append(label)

        if sentences == 0:
            raise DataValidationError(f" No valid sentences found in {file_path}")

        print(f" Validated {sentences} sentences with {errors} issues in {os.path.basename(file_path)}")
        return True


    def cross_validate_splits(self, train_file: str, dev_file: str, test_file: str):
        """Ensures all splits use consistent label sets."""
        def extract_labels(path):
            labels = set()
            with open(path, encoding="utf-8") as f:
                for line in f:
                    if line.strip() and "\t" in line:
                        labels.add(line.strip().split("\t")[1])
            return labels

        train_labels = extract_labels(train_file)
        dev_labels = extract_labels(dev_file)
        test_labels = extract_labels(test_file)

        all_labels = train_labels | dev_labels | test_labels
        inconsistent = (dev_labels | test_labels) - train_labels

        print(f" Labels found: {len(all_labels)} total")
        if inconsistent:
            print(f" Warning: Some labels appear only in dev/test: {inconsistent}")
        else:
            print("Label schema consistent across splits")

        return all_labels


def check_validation(data_dir:str):
    validator = NERDataValidator()

    train_file = os.path.join(data_dir, "train.tsv")
    dev_file = os.path.join(data_dir, "dev.tsv")
    test_file = os.path.join(data_dir, "test.tsv")

    print("\n Validating dataset files...")
    validator.validate_tsv_file(train_file)
    validator.validate_tsv_file(dev_file)
    validator.validate_tsv_file(test_file)

    label_set = validator.cross_validate_splits(train_file, dev_file, test_file)
    print(f" Total unique labels: {label_set}\n")