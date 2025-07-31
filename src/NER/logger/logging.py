from src.NER import components
import logging

import yaml
import logging.config

def setup_logging(config_path='log_config.yaml'):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)
