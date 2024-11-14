# Import the dataframes from the dala_loading file
from data_loading import dataframes
# Import the necessary modules
import logging
import pandas as pd
import numpy as np

"""Need to fix this logging arguments values due to a collision with data_processing.log"""
# Set up logging configuration
logging.basicConfig(
    filename="logs/data_filtering.log",
    filemode="w",
    format="%(levelname)s: %(message)s",
    level=logging.DEBUG
    )

logger = logging.getLogger()


# Create a filert by rating function that filter the movies based on their rating
def filter_by_rating(min_rating: float, max_rating: float = 5, inplace = False):
    """Filter the rating csv file based on the rating
    
    min_rating:
    - Define the rating on which the filter will start up [min_rating, 5]

    max_rating:
    - Define the rating on which the filter will stop [min_rating, max_rating] to default value is 5

    inplace:
    -boolean value that either return a copy of the filtred DataFrame or not, default value is set to False
    """
    try:
        df = dataframes["ratings"] if inplace else dataframes["ratings"].copy()
        df = df[np.logical_and(df["rating"] >= min_rating, df["rating"] <= max_rating)]
        logger.debug(f"The rating.csv file was filtred")
        return df.to_csv("data/processed/filtered_ratings.csv")
    except ValueError as e:
        logger.error(f"{e}: the value of one of the parameter caused error.")

filter_by_rating(3, 5)