from src.utils.logging import get_logger

def test_no_duplicate_handlers():
    logger1 = get_logger("test_logger")
    logger2 = get_logger("test_logger")
    
    assert len(logger2.handlers) == 2