from src.NER.logger import logging
from src.NER.exception import NerException
import sys
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from src.NER.constants import *
#from src.NER.config.configuration import Configuration

class DataIngestion() :
    def __init__(self,url:str = None)->str:
        self.url = url
        
    

class Artifact():
    def __init__(self,artifact:str = None) :
        self.artifact = artifact

@dataclass
class Experiment:
    experiment_id: str = None
    initialization_timestamp: datetime = None
    artifact_time_stamp: datetime = None
    running_status: str = None
    start_time: Optional[datetime] = None
    stop_time: Optional[datetime] = None
    execution_time: Optional[float] = None
    message: Optional[str] = None
    experiment_file_path: Optional[str] = None
    accuracy: Optional[float] = None
    is_model_accepted: Optional[bool] = None

    def mark_started(self):
        self.start_time = datetime.now()
        self.running_status = "RUNNING"

    def mark_completed(self, accuracy: float, accepted: bool, message: str = None):
        self.stop_time = datetime.now()
        self.execution_time = (self.stop_time - self.start_time).total_seconds() if self.start_time else None
        self.accuracy = accuracy
        self.is_model_accepted = accepted
        self.running_status = "COMPLETED"
        self.message = message or "Execution completed successfully."

    def to_dict(self):
        return {
            "experiment_id": self.experiment_id,
            "initialization_timestamp": self.initialization_timestamp.isoformat(),
            "artifact_time_stamp": self.artifact_time_stamp.isoformat(),
            "running_status": self.running_status,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "stop_time": self.stop_time.isoformat() if self.stop_time else None,
            "execution_time": self.execution_time,
            "message": self.message,
            "experiment_file_path": self.experiment_file_path,
            "accuracy": self.accuracy,
            "is_model_accepted": self.is_model_accepted,
        }