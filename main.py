from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import Traning_Pipeline_Config
from networksecurity.components.data_validation import Datavalidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
import sys


if __name__ == '__main__':
    try:
        trainingpipelineconfig = Traning_Pipeline_Config()
        data_ingestion_config=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info('Intiate the data ingestion')
        dataingestionartifact = data_ingestion.intiate_data_ingestion()
        logging.info('data ingestion is completed')
        print(dataingestionartifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = Datavalidation(dataingestionartifact,data_validation_config)
        logging.info('Intiate the data validation')
        data_validation_artifact = data_validation.intiate_data_validation()
        logging.info('data validation completed')
        print(data_validation_artifact)

        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info('data Transformation started')
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.intiate_data_transformation()
        print(data_transformation_artifact)
        logging.info('data transformation completed')

        logging.info('Model Training started')
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.intiate_model_trainer()
        logging.info('Model Training Completed')
    except Exception as e:
        raise NetworkSecurityException(e,sys)