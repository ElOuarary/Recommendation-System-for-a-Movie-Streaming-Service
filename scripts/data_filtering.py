# Import the dataframes from the dala_loading file
from data_loading import dataframes
# Import the necessary modules
import logging
import pandas as pd
import numpy as np


# Set up a logger specific to this module
logger = logging.getLogger("data_filtering")
logger.setLevel(logging.DEBUG)
logger.propagate = False

# Prevent duplicate handlers
if not logger.hasHandlers():
    # Set logging handler for this module
    file_handler = logging.FileHandler("logs/data_filtering.logs")
    file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(file_handler)


# Create a filert by rating function that filter the movies based on their rating
def filter_by_rating(min_rating: float, max_rating: float = 5, inplace = False):
    """Filter the rating csv file based on the rating

    Parameters:
        min_rating (float): Define the rating on which the filter will start up [min_rating, 5].
        max_rating (float): Define the rating on which the filter will stop [min_rating, max_rating] to default value is 5.
        inplace (bool): Whether to modify the 'ratings' DataFrame in place. Default is False.
    
    Return:
        pd.DataFrame: The filtered DataFrame (or None if inplace=True).
    """
    try:
        df: pd.DataFrame = dataframes["ratings"] if inplace else dataframes["ratings"].copy()
        df = df[np.logical_and(df["rating"] >= min_rating, df["rating"] <= max_rating)]
        logger.debug(f"The rating.csv file was filtred")
        return df.to_csv("data/processed/filtered_by_rating.csv")
    except ValueError as e:
        logger.error(f"{e}: the value of one of the parameter caused error.")


def filter_by_occurency(column: str ,min_occurence: int = 20, inplace=False):
    """
    Filter rows in the 'ratings' DataFrame based on the minimum occurrence of unique values in a specified column.

    Parameters:
        column (str): The column to analyze for occurrences.
        min_occurence (int, optional): The minimum number of occurrences required to retain a row. Default is 20.
        inplace (bool, optional): Whether to modify the 'ratings' DataFrame in place. Default is False.

    Return:
        pd.DataFrame: The filtered DataFrame (or None if inplace=True). 
    """
    try:
        
        df: pd.DataFrame = dataframes["ratings"] if inplace else dataframes["ratings"].copy()

        value_counts: pd.Series = df[column].value_counts()
        mask = value_counts > min_occurence
        filtred_df = df[df[column].isin(mask.index)]
        
        logger.info(f"Filtred '{column}' by minimum occurence of {min_occurence}")
        if filtred_df.empty:
            logger.warning(f"The Dataframe is empty after filtering")
        else:
            logger.info(f"Rows retained after filtering: {len(filtred_df)}")

        filtred_df.to_csv(f"data/processed/filtred_by_{column}_occurence.csv")
        return filtred_df if not inplace else None
    except KeyError as e:
        logger.error(f"Column Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")


filter_by_rating(3, 5)

filter_by_occurency("userId")

filter_by_occurency("movieId")