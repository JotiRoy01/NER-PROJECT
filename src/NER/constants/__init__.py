# __init__.py for constants
import os,sys
#Data Ingestion config 
CONFIG_FILE_PATH = "/config/config.yaml"
DATA_INGESTION = "data_ingestion"
URL = "url"
ROOT_DIR = os.getcwd()
ARTIFACTS_DIR = "artifacts_dir"
DATA = "data"

#Experiment
EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"

#dataset
DATASET = 'dataset'
TRAIN_PATH = "train_path"
TEST_PATH = 'test_path'
DEV_PATH = "dev_path"
MAX_LENGTH = 'max_length'

#model
PRETRAINED_MODEL = 'dmis-lab/biobert-base-cased-v1.1'
NUM_LABELS = 3

#training
BATCH_SIZE = 16
EPOCHS = 5
LEARNING_RATE = 'learning_rate'
OUTPUT_DIR = 'Artifacts/biobert_model'
LOGGING_STEP = 'logging_steps'