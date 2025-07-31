# __init__.py for exception
import sys
import traceback
import logging
#from load_logging_config import setup_logging

# Apply YAML-based logging config
setup_logging()
logger = logging.getLogger("Ner_logger")


class NerException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(str(error_message))
        self.log_data = self.get_log_dict(error_message, error_detail)
        self.error_message = str(error_message)
        self.log_error()

    @staticmethod
    def get_log_dict(error_message: Exception, error_detail: sys) -> dict:
        exc_type, _, exc_tb = error_detail.exc_info()
        tb_info = traceback.extract_tb(exc_tb)[-1]

        return {
            "file": tb_info.filename,
            "function": tb_info.name,
            "line": tb_info.lineno,
            "code": tb_info.line.strip() if tb_info.line else "N/A",
            "error_type": exc_type.__name__,
            "message": str(error_message)
        }

    def log_error(self):
        logger.error(self.log_data)

    def __str__(self):
        return str(self.log_data)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.log_data})"
