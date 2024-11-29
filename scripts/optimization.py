# Import the dataframes from the dala_loading file
from data_loading import dataframes
# Import the necessary modules to optimize the data
import logging
import pandas as pd


# Set up a logger specific to this module
logger = logging.getLogger("data_optimization")
logger.setLevel(logging.DEBUG)
logger.propagate = False

# Prevent duplicate handlers
if not logger.hasHandlers():
    # Set logging handler for this module
    file_handler = logging.FileHandler("logs/data_optimization.txt")
    file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(file_handler)


# Define a function that optimize the memory usage
def optimize_memory(name: str, df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:
    """Optimize the memory usage of the DataFrame object.

    Parameters:

        name(str): name of the file to optimize.
        df (DataFrame): DataFrame associeted to the file name
        inplace (bool): Whether to modify the DataFrame in place. Default is False.
    """
    df: pd.DataFrame = df if inplace else df.copy()
    # Optimize the integers and floats colums
    for col in df.select_dtypes(include=["int", "float"]).columns:
        old_type = df[col].dtype
        df[col] = pd.to_numeric(df[col], downcast="integer")
        logger.debug(f"Column {col} converted from {old_type} to {df[col].dtype}")

    # Optimize object columns (strings), especially for categorical data
    for col in df.select_dtypes(include="object").columns:
        num_unique_values = df[col].nunique()
        num_total_values: int = len(df[col])
        if num_unique_values / num_total_values < 0.5:
            old_dtype = df[col].dtype
            df[col] = df[col].astype("category")
            logger.debug(f"Column {col} converted from {old_dtype} to {df[col].dtype}")

    logger.info(f"Memory optimization complete for {name}.csv.")
    return df


# Log the information about each dataframe memory before and after optimization 
for name, df in dataframes.items():
    logger.info(f"The memory usage of {name}: {df.memory_usage(deep=True).sum()/1024 ** 2:.2f}MB")
    optimize_memory(name, df)
    logger.info(f"The memory usage of {name} after optimizating: {df.memory_usage(deep=True).sum()/1024 ** 2:.2f}MB\n")