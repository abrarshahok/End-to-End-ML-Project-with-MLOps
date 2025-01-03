import os
import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet
from src.mlProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)

        train_x =  train_data.drop(columns=[self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]

        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        model.fit(train_x, train_y)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
