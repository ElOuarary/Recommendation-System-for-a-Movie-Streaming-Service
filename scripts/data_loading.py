import logging
import pandas as pd
import os


# Set up logging configuration
logging.basicConfig(
    filename="logs/data_processing.log",
    filemode="w",
    format="%(levelname)s: %(message)s",
    level=logging.INFO
    )

logger = logging.getLogger()


# Define a function to load and inspect a dateset in a csv file
def load_and_inspect(file_path: str) -> pd.DataFrame:
    """
    Load and inspect the dataset in a csv file

    Logs:
    - Information about the dataset's columns, data types, shape, missing values, and duplicated rows.
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
    logger.info(f"Summary Statistics: {df.describe()}\n")
    
    return df



# Load and inspect each dataset
datasets = {
    "links": os.path.join("data", "raw", "links.csv"),
    "movies": os.path.join("data", "raw", "movies.csv"),
    "ratings": os.path.join("data", "raw", "ratings.csv"),
    "tags": os.path.join("data", "raw", "tags.csv"),
}

dataframes = {name: load_and_inspect(file_path) for name, file_path in datasets.items()}