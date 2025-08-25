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
        self.config = Configuration()
        super().__init__()
    
    def run(self) :

        pass