from src.logger import logging
from src.exception import ChurnException
from src import config, utils
from src.entity import config_entity, artifacts_entity
import os, sys
from src.components import data_ingestion


if __name__ == "__main__":


    # data ingestion

    training_pipeline_config = config_entity.TrainingPipeLineConfig()
    data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)

    data_ingestion=data_ingestion.Dataingestion(data_ingestion_config=data_ingestion_config)
    data_ingestion_artifacts=data_ingestion.start_data_ingestion()