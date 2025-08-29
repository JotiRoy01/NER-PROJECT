from src.NER import components
from src.NER.exception import NerException
import sys, os

from src.NER.pipeline.pipline import Pipeline
from src.NER.config.configuration import Configuration

def main() :
    try :
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))

    except Exception as e :
        raise NerException(e,sys) from e
    



if __name__ == "__main__" :
    main()