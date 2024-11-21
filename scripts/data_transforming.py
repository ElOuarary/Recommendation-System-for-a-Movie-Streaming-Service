from data_loading import dataframes
import logging
import numpy as np
import pandas as pd
from scipy.sparse import lil_matrix

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

user_mapping, user_indices = pd.factorize(df["userId"])
movie_mapping, movie_indices = pd.factorize(df["movieId"])

# Number of unique users and movies
num_users = len(user_mapping)
num_movies = len(movie_mapping)

# Step 2: Initialize a sparse matrix
user_item_matrix = lil_matrix((num_users, num_movies), dtype=np.float32)

# Step 3: Populate the sparse matrix
for user_idx, movie_idx, rating in zip(user_indices, movie_indices, df["rating"]):
    user_item_matrix[user_idx, movie_idx] = rating

# Step 4: Convert sparse matrix to a dense matrix (optional)
user_item_dense = user_item_matrix.toarray()

# Output the dense user-item matrix for inspection (optional)
print(user_item_dense)