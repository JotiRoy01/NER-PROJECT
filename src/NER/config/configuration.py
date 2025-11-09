#from src.NER.constants import URL, DATA_INGESTION
from src.NER.exception import NerException
from src.NER.entity.config_entity import DataIngestion, Artifact, DataLoaderArtifacts, Dataset_dir, Model_name, Training
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
    
    def dataset_tsv_dir(self) -> Dataset_dir : 
        self.train_path_tsv = os.path.join(self.artifact_dir_path.artifact, self.config_file_path[DATASET][TRAIN_PATH])
        self.test_path_tsv = os.path.join(self.artifact_dir_path.artifact, self.config_file_path[DATASET][TEST_PATH])
        self.dev_path_tsv = os.path.join(self.artifact_dir_path.artifact, self.config_file_path[DATASET][DEV_PATH])
        self.max_lenght = 128

        tsv_dataset_dir = Dataset_dir(self.train_path_tsv, self.test_path_tsv, self.dev_path_tsv, self.max_lenght)
        return tsv_dataset_dir
    
    def huggingface_model(self) -> Model_name :
        self.model_name = self.config_file_path[MODEL][PRETRAINED_MODEL]
        self.num_labels = self.config_file_path[MODEL][NUM_LABELS]
        model_name = Model_name(self.model_name, self.num_labels)
        return model_name

    def training_variables(self) -> Training :
        self.batch_size = self.config_file_path[TRAINING][BATCH_SIZE]
        self.epochs = self.config_file_path[TRAINING][EPOCHS]
        self.learning_rate = self.config_file_path[TRAINING][LEARNING_RATE]
        self.output_dir = os.path.join(self.artifact_dir_path.artifact,self.config_file_path[TRAINING][OUTPUT_DIR])
        self.logging_steps = self.config_file_path[TRAINING][LOGGING_STEP]
        train_variables = Training(self.batch_size, self.epochs,self.learning_rate,self.output_dir,self.logging_steps)
        return train_variables

    def data_loader_artifacts(self) -> DataLoaderArtifacts :
        # self.root_dir = ROOT_DIR
        # artifact_dir = os.path.join(self.root_dir, self.config_file_path[DATA_INGESTION][ARTIFACTS_DIR])
        self.artifact_dir_path.artifact
        data_dir = os.path.join(self.artifact_dir_path.artifact, self.config_file_path[DATA_INGESTION][DATA])
        data_dir = DataLoaderArtifacts(data_loader_artifacts=data_dir)
        #print(f"data dir = {data_dir}")
        return data_dir

        

