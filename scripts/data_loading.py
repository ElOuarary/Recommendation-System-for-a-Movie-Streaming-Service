# Import the necessary modules to load the data
import logging
import pandas as pd
import os


# Set up a logger specific to this module
logger = logging.getLogger("data_loading")
logger.setLevel(logging.INFO)
logger.propagate = False

# Prevent duplicate handlers
if not logger.hasHandlers():
    # Set logging handler for this module
    file_handler = logging.FileHandler("logs/data_laoding.txt", mode="w")
    file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(file_handler)


# Define a function to load and inspect a dateset in a csv file
def load_and_inspect(file_path: str) -> pd.DataFrame:
    """
    Load and inspect the dataset from a csv file.

    Parameters:
        file_path (str): The path to the csv file to be loaded.

    Returns:
        pd.DataFrame: The loaded DataFrame.

    Logs:
        Information about the dataset's columns, data types, shape, missing values, and duplicated rows.
    """
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return pd.DataFrame()

    df: pd.DataFrame = pd.read_csv(file_path)

    logger.info(f"General Information about {file_path.split("/")[-1]}")
    logger.info(f"Columns: {df.columns.to_list()}")
    logger.info(f"Data Types:\n{df.dtypes}")
    logger.info(f"Shape: {df.shape}")
    logger.info(f"Missing Values: {df.isnull().all().all()}")
    logger.info(f"Duplicated Rows: {df.duplicated().any()}")
    logger.info(f"Summary Statistics:\n{df.describe()}\n")
    
    return df



# Load and inspect each dataset
datasets = {
    "links": os.path.join("data", "raw", "links.csv"),
    "movies": os.path.join("data", "raw", "movies.csv"),
    "ratings": os.path.join("data", "raw", "ratings.csv"),
    "tags": os.path.join("data", "raw", "tags.csv"),
}

dataframes = {name: load_and_inspect(file_path) for name, file_path in datasets.items()}