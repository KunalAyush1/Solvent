import sys

class SolventException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
    
    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        tb = error_detail.exc_info()[2]
        filename = tb.tb_frame.f_code.co_filename
        line = tb.tb_lineno
        return f"Error occured in python script [{filename}] at line number [{line}]: {error_message}"
        
    def __str__(self):
        return self.error_message