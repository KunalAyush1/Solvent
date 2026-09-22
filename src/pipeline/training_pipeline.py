from src.entity.ingestion_entity import DataIngestionConfig
from src.components.data_ingestion import data_ingestion
from src.utils.logging import get_logger

logger = get_logger(__name__)

def training_pipeline():
    ingestion_config = DataIngestionConfig(
        raw_data_path="data/raw/", #put the csv file name in the path
        output_dir="data/processed"
    )
    ingestion_artifact = data_ingestion(ingestion_config)
    
    logger.info(f"Pipeline: ingestion produced {ingestion_artifact.row_count} rows")
    return ingestion_artifact

if __name__ == "__main__":
    training_pipeline()