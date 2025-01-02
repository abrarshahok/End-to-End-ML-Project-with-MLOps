from src.mlProject.components.data_validation import DataValidation
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject import logger

STAGE_NAME = 'Data Validation Stage'

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config_mgr = ConfigurationManager()
        data_validation_config = config_mgr.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
        pipeline = DataValidationPipeline()
        pipeline.main()
        logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
        raise e