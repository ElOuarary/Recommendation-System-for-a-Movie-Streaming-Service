# Import the dataframes from the dala_loading file
from data_loading import dataframes
# Import the necessary modules
import logging
import pandas as pd

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
def filter_by_rating(rating: float, inplace = False):
    """Filter the rating csv file based on the rating
    
    rating:
    - Define the rating on which the filter will start up to 5 maximun

    inplace:
    -boolean value that either return a copy of the filtred DataFrame or not, default value is set to False
    """
    df = dataframes["ratings"] if inplace else dataframes["ratings"].copy()
    df = df[df["rating"] >= rating]
    logger.debug(f"The rating.csv file was filtred")
    return df.to_csv("data/processed/filtered_ratings.csv")

filter_by_rating(5)