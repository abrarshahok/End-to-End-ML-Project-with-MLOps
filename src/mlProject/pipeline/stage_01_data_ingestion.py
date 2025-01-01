from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config_mgr = ConfigurationManager()
        data_ingestion_config = config_mgr.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        shouldExtract =  data_ingestion.download_data()
        if shouldExtract:
            data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
        raise e