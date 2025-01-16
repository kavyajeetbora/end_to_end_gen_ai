import logging
import os
from datetime import datetime

# Configure logging settings:
# - level=logging.DEBUG: Capture all messages of level DEBUG and above.
# - format: Specifies log message format:
#   - %(asctime)s: Timestamp of the log.
#   - %(levelname)s: Logging level (DEBUG, INFO, etc.).
#   - %(message)s: The log message content.

LOG_DIR_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR_PATH, exist_ok=True)


log_filename = f'''log-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'''
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, log_filename)

logging.basicConfig(
    level=logging.INFO,
    filename = LOG_FILE_PATH, 
    format='%(asctime)s - %(levelname)s - %(message)s'  
)


## TESTING
# if __name__ == "__main__":
#     # Example log messages
#     logging.debug("This is a debug message.")  # Detailed debugging information
#     logging.info("This is an info message.")  # General informational message
#     logging.warning("This is a warning message.")  # Warning about potential issues
#     logging.error("This is an error message.")  # Error indicating failure
#     logging.critical("This is a critical message.")  # Severe error indicating system failure
