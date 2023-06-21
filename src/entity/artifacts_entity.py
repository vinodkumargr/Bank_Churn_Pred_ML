from src.logger import logging
from src.exception import ChurnException
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_path:str
    test_path:str