from src.logger import logging
from src.exception import ChurnException
import os, sys
import data_dump


UNWANTED_COLUMNS = ["RowNumber","CustomerId","Surname","Age"]

DATA_INGESTION_TRAIN = "ingestion_train.csv"
DATA_INGESTION_TEST = "ingestion_test.csv"
VALID_TRAIN_FILE = "valid_train.csv"
VALID_TEST_FILE = "valid_test.csv"
TRANSFORMER_TRAIN_FILE = "transform_train.csv"
TRANSFORMER_TEST_FILE = "transform_test.csv"
TRANSFORMER_OBJ_FILE = 'transformer.pkl'
DATA_OBJ_FILE = "data_obj.pkl"



class TrainingPipeLineConfig:

    def __init__(self):
        try:
            self.artifacts_dir = os.path.join(os.getcwd(),"artifacts")
        except Exception as e:
            raise ChurnException(e, sys)
        
class DataIngestionConfig:

    def __init__(self, training_pipeline_config :TrainingPipeLineConfig):
        try:

            self.data_base_name=data_dump.DATABASE_NAME
            self.collection_name=data_dump.COLLECTION_NAME

            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifacts_dir, "Data_Ingestion")
            os.makedirs(self.data_ingestion_dir,exist_ok=True)

            self.train_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_TRAIN)
            self.test_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_TEST)

        except Exception as e:
            raise ChurnException(e, sys)
        
class DataValidationConfig:

    def __init__(self, training_pipeline_config:TrainingPipeLineConfig):
        try:
            self.data_validation_dir = os.path.join(training_pipeline_config.artifacts_dir, "Data_Validation")
            os.makedirs(self.data_validation_dir, exist_ok=True)

            self.valid_train_path=os.path.join(self.data_validation_dir, VALID_TRAIN_FILE)
            self.valid_test_path=os.path.join(self.data_validation_dir, VALID_TEST_FILE)

        except Exception as e:
            raise ChurnException(e, sys)
        

class DataTransformationConfig:
    def __init__(self, training_pipeline_config:TrainingPipeLineConfig):
        try:

            self.data_transformation_dir = os.path.join(training_pipeline_config.artifacts_dir, "Data_Transformation")
            os.makedirs(self.data_transformation_dir, exist_ok=True)

            self.transform_train_path = os.path.join(self.data_transformation_dir, TRANSFORMER_TRAIN_FILE)
            self.transform_test_path = os.path.join(self.data_transformation_dir, TRANSFORMER_TEST_FILE)
            self.transformer_obj_path = os.path.join(self.data_transformation_dir, TRANSFORMER_OBJ_FILE)
            self.data_obj_path = os.path.join(self.data_transformation_dir, DATA_OBJ_FILE)

        except Exception as e:
            raise ChurnException(e, sys)