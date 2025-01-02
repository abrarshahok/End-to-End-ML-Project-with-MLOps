import os
from src.mlProject import logger
from src.mlProject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def perform_train_test_split(self):
        df = pd.read_csv(self.config.data_path)
        train, test = train_test_split(df, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"Splitted data into train and test and saved at {self.config.root_dir}")
        logger.info(f"train shape: {train.shape}, test shape: {test.shape}")
    
    