import mlflow
import joblib
import dagshub
import numpy as np
import pandas as pd
import mlflow.sklearn
from pathlib import Path
from urllib.parse import urlparse
from mlflow.models import ModelSignature
from mlflow.types.schema import Schema, ColSpec
from src.mlProject.utils.common import save_json
from src.mlProject.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, preds):
        rmse = np.sqrt(mean_squared_error(actual, preds))
        mae = mean_absolute_error(actual, preds)
        r2 = r2_score(actual, preds)
        return rmse, mae, r2

    def log_into_mlflow(self):
        dagshub.init(repo_owner='abrarshahok', repo_name='End-to-End-ML-Project-with-MLOps', mlflow=True)

        experiment = mlflow.get_experiment_by_name(self.config.experiment_name)
        if experiment is None:
            mlflow.create_experiment(self.config.experiment_name)
        mlflow.set_experiment(self.config.experiment_name)
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[self.config.target_column]
        
        signature, input_example = self._get_model_signature_and_input_example(test_x)

        tracking_url_type_store = urlparse(mlflow.get_registry_uri()).scheme

        with mlflow.start_run():
            preds = model.predict(test_x)
            
            (rmse, mae, r2) = self.eval_metrics(test_y, preds)

            scores = {
                "rmse": rmse,
                "mae": mae,
                "r2": r2
            }

            save_json(path=Path(self.config.metrics_path), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    model, 
                    "model", 
                    signature=signature,
                    input_example=input_example,
                    registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(
                    model, 
                    "model", 
                    signature=signature,
                    input_example=input_example)

    def _get_model_signature_and_input_example(self, test_x):
        input_schema = Schema([
            ColSpec("double", col) for col in test_x.columns
        ])
        output_schema = Schema([ColSpec("long", self.config.target_column)])
        signature = ModelSignature(inputs=input_schema, outputs=output_schema)
        input_example = test_x.head(1)
        return signature, input_example
