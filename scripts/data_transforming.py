"""
Script: data_transforming.py
Purpose: Transform rating data into a normalized user-item matrix for recommendation systems.
"""

from data_loading import dataframes
from data_filtering import filter_by_occurency, filter_by_rating
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


try:
    # Data preparation
    df: pd.DataFrame = filter_by_rating(dataframes["ratings"], 4)
    df = filter_by_occurency(df, "userId", 400)
    user_mapping, user_indices = pd.factorize(df["userId"])
    movie_mapping, movie_indices = pd.factorize(df["movieId"])

    # Get the number of unique users and movies
    num_users: int = user_indices.max()
    num_movies: int = movie_indices.max()
    logger.info(f"Number of unique users: {num_users}, Number of unique movies: {num_movies}")

    # Initialize a sparse matrix and fill it
    user_item_matrix = lil_matrix((num_users, num_movies))
    for user_idx, movie_idx, rating in zip(user_mapping, df["movieId"] - 1, df["rating"]):
        user_item_matrix[user_idx, movie_idx] = rating

    
    # Normalization the output
    user_item_dense = user_item_matrix.toarray()
    row_means: np.ndarray = np.mean(user_item_dense, axis=1, keepdims=True, where=(user_item_dense!=0))
    rounded_means: np.ndarray = np.round(row_means, 2)
    normalized_user_item: np.ndarray = np.subtract(user_item_dense, rounded_means, where=(user_item_dense!=0))
    
    # Load the output to a csv file if "data/processed"
    pd.DataFrame(normalized_user_item, dtype=np.float32).to_csv("data/processed/output.csv")
    logger.info(f"Normalized matrix saved to data/processed/output.csv")

except Exception as e:
    logger.error(f"Error during data transformation: {e}")