import logging
from distutils.command.config import config

from src.NER.constants import *
from src.NER.exception import NerException, logger

from src.NER.config.configuration import Configuration
from src.NER.entity.config_entity import Experiment, DataLoaderArtifacts, Artifact
from src.NER.components.data_loader import prepare_bc5cdr_dataset
from src.NER.components.data_validation import check_validation
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
            os.makedirs(config.artifact_dir().artifact, exist_ok=True)
            Pipeline.experiment_file_path = os.path.join(config.artifact_dir().artifact,EXPERIMENT_DIR_NAME,EXPERIMENT_FILE_NAME)
            print(Pipeline.experiment_file_path )
            logger.info(f"experiment file path is created at {Pipeline.experiment_file_path}")
            #config.data_loader_artifacts()
            config.dataset_tsv_dir()
            
            super().__init__(daemon=False, name="Pipeline")
            self.config = config
        except Exception as e :
            raise NerException(e,sys) from e
        
    
    
    # def start_data_ingestion(self) :
    #     raw_dir = "Artifacts\\data\\bc5cdr\\CDR_Data"
    #     prepare_bc5cdr_dataset(raw_dir=raw_dir, out_dir=self.config.data_loader_artifacts().data_loader_artifacts)

    # def data_validation(self):
    #     data_dir = "Artifacts\\data"
    #     check_validation(data_dir)
    # def run(self) :
    #     try :
    #         self.run_pipeline()
    #     except Exception as e:
    #         raise NerException


        