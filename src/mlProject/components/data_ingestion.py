import os
from pathlib import Path
from urllib import request
import zipfile
from src.mlProject import logger
from src.mlProject.entity.config_entity import DataIngestionConfig
from src.mlProject.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        """
        
        Downloads the data from the source URL if it doesn't exist

        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                self.config.source_URL, 
                self.config.local_data_file)
            logger.info(f"{filename} downloaded!\nInfo: {headers}")
            return True
        else:
            logger.info(f"Data already exists at {self.config.local_data_file} with size {get_size(Path(self.config.local_data_file))}")
            return False
    
    def extract_zip_file(self):
        """
        Extracts the zip file to the specified directory

        """
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Data extracted at {self.config.unzip_dir}")