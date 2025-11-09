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
MODEL = "model"
PRETRAINED_MODEL = 'pretrained_model'
NUM_LABELS = 'num_labels'

#training
TRAINING = 'training'
BATCH_SIZE = 'batch_size'
EPOCHS = 'epochs'
LEARNING_RATE = 'learning_rate'
OUTPUT_DIR = 'output_dir'
LOGGING_STEP = 'logging_steps'