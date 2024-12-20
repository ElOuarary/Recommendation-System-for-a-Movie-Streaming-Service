# Import the dataframes from the dala_loading file
from data_loading import dataframes
# Import the necessary modules to filter the data
import logging
import pandas as pd
import numpy as np


# Set up a logger specific to this script
logger = logging.getLogger("data_filtering")
logger.setLevel(logging.DEBUG)
logger.propagate = False

# Prevent duplicate handlers
if not logger.hasHandlers():
    # Set logging handler for this script
    file_handler = logging.FileHandler("logs/data_filtering.txt", mode="w")
    file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(file_handler)


# Create a filert by rating function that filter the movies based on their rating
def filter_by_rating(dataframe: pd.DataFrame, min_rating: float, max_rating: float = 5, inplace = False):
    """Filter the rating csv file based on the rating

    Parameters:
        min_rating (float): Define the rating on which the filter will start up [min_rating, 5].
        max_rating (float): Define the rating on which the filter will stop [min_rating, max_rating] to default value is 5.
        inplace (bool): Whether to modify the 'ratings' DataFrame in place. Default is False.
    
    Return:
        pd.DataFrame: The filtered DataFrame (or None if inplace=True).
    """
    try:
        # load the dataframe of rating and either make a copy or view of it based on inplace parameter value
        df: pd.DataFrame = dataframe if inplace else dataframe.copy()
        # filter the dataframe based on the specific intervale
        filtred_df: pd.DataFrame = df[np.logical_and(df["rating"] >= min_rating, df["rating"] <= max_rating)]

        # Log a message based of the filtred dataframe
        logger.debug(f"The rating.csv file was filtred in the range [{min_rating}, {max_rating}]")
        if filtred_df.empty:
            logger.warning(f"The Dataframe is empty after filtering")
        else:
            logger.info(f"Rows retained after filtering: {len(filtred_df)}")

        # Load the dataframe into a specific csv file
        filtred_df.to_excel(f"data/processed/filtred_by_rating.xlsx", index=False)
        return filtred_df if not inplace else None
    # Handle different error
    except ValueError as e:
        logger.error(f"{e}: the value of one of the parameter caused error.")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")


def filter_by_occurency(dataframe: pd.DataFrame, inplace=False):
    """
    Filter rows in the 'ratings' DataFrame based on the minimum occurrence of unique values in a specified column.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame.
        inplace (bool, optional): Whether to modify the 'ratings' DataFrame in place. Default is False.

    Return:
        pd.DataFrame: The filtered DataFrame (or None if inplace=True). 
    """
    try:
        # Load either a copy or a veiw of the ratings dataframe based of the inplace parameter value
        df: pd.DataFrame = dataframe if inplace else dataframe.copy()
        
        # Get the average occurence for both userId and movieId in the ratings csv file
        avg_user_occ, avg_movie_occ = get_average_occurency(df)

        # Filter the dataframe based on the occurency for each
        valid_users = df["userId"].value_counts()[lambda x: x > avg_user_occ].index
        valid_movies = df["movieId"].value_counts()[lambda x: x > avg_movie_occ].index
        filtred_df: pd.DataFrame = df[(df["userId"].isin(valid_users)) & (df["movieId"].isin(valid_movies))]
        
        # Log a message based of the filtred dataframe
        logger.info(f"Filtred Completed.")
        if filtred_df.empty:
            logger.warning(f"The Dataframe is empty after filtering")
        else:
            logger.info(f"Rows retained after filtering: {len(filtred_df)}")
        
        # Load the dataframe into a specific csv file
        filtred_df.to_excel(f"data/processed/filtred_by_occurence.xlsx", index=False)
        return filtred_df if not inplace else None
    
    # Handle different error
    except KeyError as e:
        logger.error(f"Column Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")


def get_average_occurency(dataframe: pd.DataFrame) -> np.int32:
    """
    Get the average occurency for both users that had rated less movies, and movies that where less rated 
    """
    average_userId_occurency: np.int32 = dataframe["userId"].value_counts().mean().astype(np.int32)
    average_movieId_occurency: np.int32 = dataframe["movieId"].value_counts().mean().astype(np.int32)
    return average_userId_occurency, average_movieId_occurency



filter_by_occurency(dataframes["ratings"])