from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.mlProject import logger

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f"========================================")
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<")
    logger.info(f"========================================")
except Exception as e:
    logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e