import numpy as np
import pandas as pd
from src.components.data_ingestion import Dataingestion
from src.entity import config_entity, artifacts_entity
from src.logger import logging
from src.exception import ChurnException
import sys, os
from typing import Optional
from sklearn.impute import SimpleImputer



class DataValidation:

    def __init__(self, data_validation_config:config_entity.DataValidationConfig,
                    data_ingestion_artifacts:artifacts_entity.DataIngestionArtifact):
        try:
            
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifacts=data_ingestion_artifacts

        except Exception as e:
            raise ChurnException(e,sys)



    def impute_null_values(self, df:pd.DataFrame)->Optional[pd.DataFrame]:
        try:
            
            columns_with_null = df.columns[df.isnull().any()].tolist()

            if len(columns_with_null) > 0:
                logging.info(f"Null values found: {columns_with_null}")

                imputer = SimpleImputer(strategy='most_frequent')
                for column in columns_with_null:
                    df[column] = imputer.fit_transform(df[[column]]).ravel()
                logging.info("Null values imputed")
                    
            logging.info(f"No null values found")

            return df

        except Exception as e:
            raise ChurnException(e,sys)

        
    def drop_unwaned_columns(self, df:pd.DataFrame)-> Optional[pd.DataFrame]:
        try:

            df = df.drop(columns=config_entity.UNWANTED_COLUMNS, axis=1)

            return df
        except Exception as e:
            raise ChurnException(e,sys)
               

    def initiate_data_validation(self)->artifacts_entity.DataValidationArtifact:
        try:
            logging.info("data validation started........")

            train_df = pd.read_csv(self.data_ingestion_artifacts.train_path)
            test_df = pd.read_csv(self.data_ingestion_artifacts.test_path)

            
            train_df = self.impute_null_values(df=train_df)
            test_df = self.impute_null_values(df=test_df)
        
            train_df = self.drop_unwaned_columns(df=train_df)
            test_df = self.drop_unwaned_columns(df=test_df)

            train_df.to_csv(path_or_buf=self.data_validation_config.valid_train_path, index=False, header=True)
            test_df.to_csv(path_or_buf=self.data_validation_config.valid_test_path, index=False, header=True)


            logging.info("data validation is almost done")

            data_validation_artifact = artifacts_entity.DataValidationArtifact(
                valid_train_path = self.data_validation_config.valid_train_path,
                valid_test_path= self.data_validation_config.valid_test_path)
            
            logging.info("returning data_validation_artifact")


            return data_validation_artifact

        except Exception as e:
            raise ChurnException(e,sys)