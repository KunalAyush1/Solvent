from src.entity.ingestion_entity import DataIngestionConfig
from src.components.data_ingestion import data_ingestion
import os

def test_data_ingestion():
    config = DataIngestionConfig(
        raw_data_path="tests/sample.csv",
        output_dir="tests/output"
    )
    artifact = data_ingestion(config)
    
    assert artifact.row_count == 4
    assert os.path.exists(artifact.output_data_path)