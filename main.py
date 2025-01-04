from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<\n\n==========================")
except Exception as e:
    logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e

STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    pipeline = DataValidationPipeline()
    pipeline.main()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<\n\n==========================")
except Exception as e:
    logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e

STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    pipeline = DataTransformationPipeline()
    pipeline.main()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<\n\n==========================")
except Exception as e:
    logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e

STAGE_NAME = 'Model Trainer Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    pipeline = ModelTrainerPipeline()
    pipeline.main()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<\n\n==========================")
except Exception as e:
    logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e

STAGE_NAME = 'Model Evaluation Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    pipeline = ModelEvaluationPipeline()
    pipeline.main()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<\n\n==========================")
except Exception as e:
    logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e