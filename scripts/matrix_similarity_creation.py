import logging
import os
import numpy as np
import pandas as pd

import sys


# Set the logger for this scirpt
logger = logging.getLogger("Similarity movies matrix")
logger.setLevel(logging.DEBUG)
logger.propagate(False)

# Set the handler for this scipt
if not logger.hasHandlers():
    file_handler = logging.FileHandler("data/similarity_movie_matrix.csv")
    file_handler.setFormatter(logging.Formatter("%(level)s: %(message)s"))
    logger.addHandler(file_handler)


# Load the user item matrix from the foalder data
if not os.path.exists("data/similarity_movie_matrix.csv"):
    logger.info("The user item matrix was not created.")
    sys.exit()