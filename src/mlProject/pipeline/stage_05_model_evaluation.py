from src.mlProject.components.model_evaluation import ModelEvaluation
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject import logger

STAGE_NAME = 'Model Evaluation Stage'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self): 
        config_mgr = ConfigurationManager()
        model_evaluation_config = config_mgr.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
        pipeline = ModelEvaluationPipeline()
        pipeline.main()
        logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(f"Stage {STAGE_NAME} failed with error: {str(e)}")
        raise e