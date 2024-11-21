import logging
from numpy import matrix
import pandas as pd


# Set up a logger specific to this module
logger = logging.getLogger("data transforming")
logger.setLevel(logging.DEBUG)
logger.propagate = False

# Prevent duplicate handler
if not logger.hasHandlers():
    # Set logging handler for this module
    file_handler = logging.Handler("data/processed/data_transformed.logs")
    file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(file_handler)


