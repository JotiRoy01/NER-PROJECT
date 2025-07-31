import yaml
#from housing.exception import Housing_Exception
import os, sys

def read_yaml_file(file_path:str) -> dict :
    """
    reads a yaml file and returns the containers as a dictionary file_path: str
    """
    try:
        with open(file_path, "rb") as yaml_file :
            config_info = yaml.safe_load(yaml_file)
            return config_info

    except Exception as e:
        raise Housing_Exception(e, sys) from e