from src.logger import logging
from src.exception import ChurnException
from src import config, utils
from src.entity import config_entity, artifacts_entity
import os, sys
from src.components.data_ingestion import Dataingestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation


if __name__ == "__main__":


    # data ingestion

    training_pipeline_config = config_entity.TrainingPipeLineConfig()
    data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)

    data_ingestion=Dataingestion(data_ingestion_config=data_ingestion_config)
    data_ingestion_artifact=data_ingestion.start_data_ingestion()


    # data validation:

    data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
    data_validation= DataValidation(data_validation_config=data_validation_config,
                                        data_ingestion_artifacts=data_ingestion_artifact)
    data_validation_artifact=data_validation.initiate_data_validation()


    # data transformation:

    data_transformation_config=config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
    data_transformation = DataTransformation(data_transformation_cofig=data_transformation_config,
                                                    data_validation_artifacts=data_validation_artifact)
        
    data_transformation_artifact=data_transformation.initiate_data_transformation()
