# Import the dataframes from the dala_loading file
from data_loading import dataframes
# Import the necessary modules
import logging
import pandas as pd


# Set up logging configuration
logging.basicConfig(
    filename="logs/data_processing.log",
    filemode="w",
    format="%(levelname)s: %(message)s",
    level=logging.DEBUG
    )

logger = logging.getLogger()


# Define a function that optimize the memory usage
def optimize_memory(name: str, df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:
    """Optimize the memory usage of the DataFrame object

    name:

    -name of the file that you will optimize

    df:

    -DataFrame associeted to the file name

    inplace:

    -boolean value that either return a copy of the otptimized DataFrame or not, default value is set to True
    """
    df = df if inplace else df.copy()
    # Optimize the integers and floats colums
    for col in df.select_dtypes(include=["int", "float"]).columns:
        old_type = df[col].dtype
        df[col] = pd.to_numeric(df[col], downcast="integer")
        logger.debug(f"Column {col} converted from {old_type} to {df[col].dtype}")

    # Optimize object columns (strings), especially for categorical data
    for col in df.select_dtypes(include="object").columns:
        num_unique_values = df[col].nunique()
        num_total_values = len(df[col])
        if num_unique_values / num_total_values < 0.5:
            old_dtype = df[col].dtype
            df[col] = df[col].astype("category")
            logger.debug(f"Column {col} converted from {old_dtype} to {df[col].dtype}")

    logger.info(f"Memory optimization complete for {name}.csv.")
    return df


for name, df in dataframes.items():
    logger.info(f"The memory usage of {name}: {df.memory_usage(deep=True).sum()/1024 ** 2:.2f}MB")
    optimize_memory(name, df)
    logger.info(f"The memory usage of {name} after optimizating: {df.memory_usage(deep=True).sum()/1024 ** 2:.2f}MB\n")