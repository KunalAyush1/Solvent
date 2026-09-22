from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str
    output_dir: str


@dataclass
class DataIngestionArtifact:
    row_count: int
    output_data_path: str