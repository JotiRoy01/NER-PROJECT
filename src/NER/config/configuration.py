#from src.NER.constants import URL, DATA_INGESTION
from src.NER.exception import NerException
from src.NER.entity.config_entity import DataIngestion, Artifact, DataLoaderArtifacts
from src.NER.constants import *
from src.NER.utils.util import read_yaml_file
import sys

class Configuration() :
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH)->None:
        try :
            self.config_file_path = read_yaml_file(file_path=config_file_path)
            self.artifact_dir_path = self.artifact_dir()
            self.data_loader_artifacts()
        except Exception as e:
            raise NerException(e,sys) from e
    
    def data_ingestion(self) ->DataIngestion :
        self.data_ingestion =  self.config_file_path[DATA_INGESTION]
        self.data_url = self.data_ingestion[URL]
        return DataIngestion(
            url=self.data_url
        )
    def artifact_dir(self) -> Artifact :
        self.config_file_path[DATA_INGESTION]
        self.root_dir = ROOT_DIR
        artifact_dir = os.path.join(self.root_dir, self.config_file_path[DATA_INGESTION][ARTIFACTS_DIR])
        artifact_dir_path = Artifact(artifact=artifact_dir)
        return artifact_dir_path
    def data_loader_artifacts(self) -> DataLoaderArtifacts :
        # self.root_dir = ROOT_DIR
        # artifact_dir = os.path.join(self.root_dir, self.config_file_path[DATA_INGESTION][ARTIFACTS_DIR])
        self.artifact_dir_path.artifact
        data_dir = os.path.join(self.artifact_dir_path.artifact, self.config_file_path[DATA_INGESTION][DATA])
        data_dir = DataLoaderArtifacts(data_loader_artifacts=data_dir)
        #print(f"data dir = {data_dir}")
        return data_dir

        

