from data_loading import dataframes
import logging
import numpy as np
import pandas as pd
import os
from scipy.sparse import lil_matrix


# Set up a logger specific to this module
logger = logging.getLogger("data_transforming")
logger.setLevel(logging.INFO)
logger.propagate = False

# Prevent duplicate handler
if not logger.hasHandlers():
    # Set logging handler for this module
    file_handler = logging.FileHandler("logs/data_transformed.txt")
    file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(file_handler)


# Create a 2-D matrix full of NaN with the users id are the number of rows and movies id are the number of columns
df = dataframes["ratings"]

user_mapping, user_indices = pd.factorize(df["userId"])
movie_mapping, movie_indices = pd.factorize(df["movieId"])

# Number of unique users and movies
num_users = user_indices.max()
num_movies = movie_indices.max()

# Initialize a sparse matrix
user_item_matrix = lil_matrix((num_users, num_movies))

# Step 3: Populate the sparse matrix
for user_idx, movie_idx, rating in zip(user_mapping, movie_mapping, df["rating"]):
    user_item_matrix[user_idx, movie_idx] = rating


# Step 4: Convert sparse matrix to a dense matrix (optional)
user_item_dense = user_item_matrix.toarray()

logger.info(user_item_dense)

# Compute the average of each row without including the NaN values
row_means = np.mean(user_item_dense, axis=1, keepdims=True, where=(user_item_dense!=0))
logger.info(row_means)

normalized_user_item = user_item_dense - row_means
logger.info(normalized_user_item)

logger.info(normalized_user_item[normalized_user_item>0])