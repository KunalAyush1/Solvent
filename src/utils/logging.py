import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

LOG_DIR = "logs" 
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if logger.handlers:
        return logger #it avoids creating multiple logger instances
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5242880, backupCount=3)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger