import sys
import pandas as pd
import os
from src.entity.ingestion_entity import DataIngestionConfig, DataIngestionArtifact
from src.utils.logging import get_logger
from src.utils.exceptions import SolventException


logger = get_logger(__name__)

def data_ingestion(config: DataIngestionConfig) -> DataIngestionArtifact:
    try:
        logger.info("Starting Data Ingestion")
        data = pd.read_csv(config.raw_data_path)
        os.makedirs(config.output_dir, exist_ok=True)
        output_file_path = os.path.join(config.output_dir, "data.csv")
        data.to_csv(output_file_path, index=False)
        
        logger.info(f"Data Ingestion Complete, {len(data)} rows ingested")
        
        return DataIngestionArtifact(
            row_count = len(data),
            output_data_path= output_file_path
        )
    
    except Exception as e:
        raise SolventException(e, sys) from e
    
        
