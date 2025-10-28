import os
import json
from datasets import load_dataset
from src.NER.utils.util import *
from src.NER.entity.config_entity import *
from src.NER.config.configuration import *

def prepare_bc5cdr_dataset(data_artifacts:DataLoaderArtifacts, save_dir="bc5cdr") :
    """
    the function auto download the dataset
    1. downlaod the dataset from hugging face
    2. local data as a json format 
    3. auto convert to the level map
    """

    download_path = os.path.join(data_artifacts.data_loader_artifacts, save_dir)
    print(download_path)
    create_directories([download_path])




if __name__ == "__main__" :
    prepare_bc5cdr_dataset()


