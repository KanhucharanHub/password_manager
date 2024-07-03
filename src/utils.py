import logging
import os

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def get_asset_path(relative_path):
    return os.path.join(os.path.dirname(__file__), '..', relative_path)