from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject import logger

STAGE_NAME = 'Model Trainer Stage'

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config_mgr = ConfigurationManager()
        model_trainer_config = config_mgr.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
        raise e