import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        model_path = Path('artifacts/model_trainer/model.joblib')
        self.model = joblib.load(model_path)
    
    def predict(self, data: pd.DataFrame) -> np.ndarray:
        preds = self.model.predict(data)
        return preds