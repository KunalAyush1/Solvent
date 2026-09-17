import sys
import pytest
from src.utils.exceptions import SolventException
def test_solvent_exception_message():
    try:
        x = 1/ 0
    except Exception as e:
        exc = SolventException(e, sys)
        assert "division by zero" in str(exc)
        assert "test_exceptions.py"