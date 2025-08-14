import yaml
#from housing.exception import Housing_Exception
import os, sys
from src.NER.exception import NerException
from src.NER.logger.logging import logging

def read_yaml_file(file_path:str) -> dict :
    """
    reads a yaml file and returns the containers as a dictionary file_path: str
    """
    try:
        with open(file_path, "rb") as yaml_file :
            config_info = yaml.safe_load(yaml_file)
            return config_info

    except Exception as e:
        raise NerException(e, sys) from e
    

def create_directories(path_to_directories:str, verbose = True) :
    """create list of directories
    Args:
        path_to_directories(list): list of path of directories
        ignore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to False)"""
    
    for path in path_to_directories :
        os.makedirs(path, exist_ok=True)
        if verbose :
            logging.info(f"created directory at : {path}")
