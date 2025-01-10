import logging
import os


def setup_logger(name, log_file, level=logging.DEBUG):
    """Function to setup a logger; can be used in multiple modules."""
    # Ensure the logs directory exists
    log_directory = os.path.join(os.path.dirname(__file__), '../logs')
    os.makedirs(log_directory, exist_ok=True)

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create file handler
    file_handler = logging.FileHandler(os.path.join(log_directory, log_file))
    file_handler.setLevel(level)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger