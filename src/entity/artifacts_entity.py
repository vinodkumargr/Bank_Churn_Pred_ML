from src.logger import logging
from src.exception import ChurnException
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_path:str
    test_path:str

@dataclass
class DataValidationArtifact:
    valid_train_path:str
    valid_test_path:str

@dataclass
class DataTransformationArtifact:
    transform_train_path:str
    transform_test_path:str
    transformer_obj_path:str