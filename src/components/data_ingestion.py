from src.logger import logging
from src.exception import ChurnException
import pandas as pd
from src import config, utils
from src.entity import config_entity, artifacts_entity
import os, sys
from sklearn.model_selection import train_test_split


class Dataingestion:

    def __init__(self, data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ChurnException(e, sys)
        
    def start_data_ingestion(self) -> artifacts_entity.DataIngestionArtifact:

        logging.info("starting data ingestion stage......")

        #df = pd.read_csv("/home/vinod/projects_1/bank_churn_pred/churn.csv")
        #df = df.copy()

        df = pd.DataFrame(utils.get_df(database_name=self.data_ingestion_config.data_base_name, 
                                       collection_name=self.data_ingestion_config.collection_name))
        
        logging.info("reading data from mongodb...")
        logging.info(f"found data shape : {df.shape}")

        x_train, x_test = train_test_split(df, test_size=0.2)

        logging.info("splitting data and storing into train and test path")

        x_train.to_csv(path_or_buf = self.data_ingestion_config.train_path, index=False, header=True)
        x_test.to_csv(path_or_buf = self.data_ingestion_config.test_path, index=False, header=True)

            
        #preparing artifacts folder:
        data_ingestion_artifact = artifacts_entity.DataIngestionArtifact(
            train_path=self.data_ingestion_config.train_path,
            test_path=self.data_ingestion_config.test_path)