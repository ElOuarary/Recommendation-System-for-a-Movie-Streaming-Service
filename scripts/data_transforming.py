from data_loading import dataframes
import logging
import numpy as np
import pandas as pd


# Set up a logger specific to this module
logger = logging.getLogger("data transforming")
logger.setLevel(logging.DEBUG)
logger.propagate = False

# Prevent duplicate handler
if not logger.hasHandlers():
    # Set logging handler for this module
    file_handler = logging.Handler("logs/data_transformed.logs")
    file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(file_handler)


# Create a 2-D matrix full of NaN with the users id are the number of rows and movies id are the number of columns
df = dataframes["ratings"]
num_rows: int = df["userId"].max()
num_columns: int = df["movieId"].max()
user_item: np.ndarray = np.full((num_rows, num_columns), np.nan)

for i in range(0, num_rows):
    mask = df["userId"] == i + 1
    user_item[i][df["movieId"][mask].values - 1] = df["rating"][mask].values

logger.info(user_item)