from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject import logger
from pathlib import Path

STAGE_NAME = 'Data Transformation Stage'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        with open(Path('artifacts/data_validation/status.txt','r')) as f:
            status = f.read().split(' ')[-1]

        if status == 'True':
            config_mgr = ConfigurationManager()
            data_transformation_config = config_mgr.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.perform_train_test_split()
        else:
            raise Exception('Your data schema is not valid')

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
        raise e