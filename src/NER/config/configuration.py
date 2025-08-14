from src.NER.constants import URL, DATA_INGESTION
from src.NER.exception import NerException
from src.NER.entity.config_entity import DataIngestion
from src.NER.constants import *
from src.NER.utils.util import read_yaml_file
import sys

class Configuraion() :
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH)->None:
        try :
            self.config_file_path = read_yaml_file(file_path=config_file_path)
            self.con
        except Exception as e:
            raise NerException(e,sys) from e
    
    def data_ingestion(self) ->DataIngestion :
        self.data_ingestion =  self.config_file_path[DATA_INGESTION]
        self.data_url = self.data_ingestion[URL]
        
    