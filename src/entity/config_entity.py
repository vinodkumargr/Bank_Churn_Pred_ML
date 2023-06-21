from src.logger import logging
from src.exception import ChurnException
import os, sys
import data_dump


data_ingestion_train = "ingestion_train.csv"
data_ingestion_test = "ingestion_test.csv"






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

            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifacts_dir, "data_ingestion")

            data_split_dir = os.path.join(self.data_ingestion_dir, "data_split")
            os.makedirs(data_split_dir, exist_ok=True)

            self.train_path = os.path.join(data_split_dir, data_ingestion_train)
            self.test_path = os.path.join(data_split_dir, data_ingestion_test)

        except Exception as e:
            raise ChurnException(e, sys)