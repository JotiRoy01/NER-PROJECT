from src.NER.constants import *
from src.NER.exception import NerException
from src.NER.logger import logging
from src.NER.config.configuration import Configuration
from src.NER.entity.config_entity import Experiment
from threading import Thread
from multiprocessing import Process
from typing import List
import os, sys
import pandas as pd


class Pipeline(Thread) :
    experiment: Experiment = Experiment()
    experiment_file_path = None
    
    def __init__(self, config:Configuration) ->None :
        try :
            os.makedirs(config.artifact_dir, exist_ok=True)
            Pipeline.experiment_file_path = os.path.join(config.artifact_dir,EXPERIMENT_DIR_NAME,EXPERIMENT_FILE_NAME)
            super().__init__(daemon=False, name="Pipeline")
            self.config = config
        except Exception as e :
            raise NerException(e,sys) from e
    
    def run(self) :



        pass