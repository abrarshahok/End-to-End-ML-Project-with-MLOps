import pandas as pd
from src.mlProject import logger
from src.mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config    
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            df = pd.read_csv(self.config.unzip_data_dir)
            
            if df.empty:
                validation_status = False
                logger.error("DataFrame is empty")
                self._save_validation_status(validation_status)
                return validation_status

            df_columns = set(df.columns)
            schema_columns = set(self.config.all_schema.keys())
            
            if not df_columns.issubset(schema_columns):
                validation_status = False
                missing_cols = df_columns - schema_columns
                logger.error(f"Missing columns in schema: {missing_cols}")
                self._save_validation_status(validation_status)
                return validation_status
            
            for column, expected_type in self.config.all_schema.items():
                actual_dtype = df[column].dtype
                if str(actual_dtype) != str(expected_type):
                    validation_status = False
                    logger.error(f"Column: {column} | Expected dtype: {expected_type} | Found dtype: {actual_dtype}")
                    self._save_validation_status(validation_status)
                    return validation_status
                        
            logger.info("Data Validation Successful.")
            self._save_validation_status(validation_status)
            return validation_status

        except Exception as e:
            logger.error(f"Validation failed: {str(e)}")
            self._save_validation_status(False)
            raise e

    def _save_validation_status(self, status: bool):
        with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation Status: {status}")