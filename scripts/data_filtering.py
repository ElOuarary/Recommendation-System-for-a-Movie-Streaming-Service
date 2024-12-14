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


def filter_by_occurency(dataframe: pd.DataFrame, column: str ,min_occurence: int = 20, inplace=False):
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
        # Load either a copy or a veiw of the ratings dataframe based of the inplace parameter value
        df: pd.DataFrame = dataframe if inplace else dataframe.copy()
        
        # Count the occurency for each value in the specifc column  and create a mask to filter the dataframe
        value_counts: pd.Series = df[column].value_counts()
        mask: pd.Series = value_counts > min_occurence
        filtred_df = df[df[column].isin(mask.index)]
        
        # Log a message based of the filtred dataframe
        logger.info(f"Filtred '{column}' by minimum occurence of {min_occurence}")
        if filtred_df.empty:
            logger.warning(f"The Dataframe is empty after filtering")
        else:
            logger.info(f"Rows retained after filtering: {len(filtred_df)}")
        
        # Load the dataframe into a specific csv file
        filtred_df.to_excel(f"data/processed/filtred_by_{column}_occurence.xlsx", index=False)
        return filtred_df if not inplace else None
    
    # Handle different error
    except KeyError as e:
        logger.error(f"Column Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")