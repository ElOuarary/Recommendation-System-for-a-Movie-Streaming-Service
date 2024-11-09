# Importing the necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Define a function to load and inspect a dateset
def load_and_inspect(file_path: str) -> pd.DataFrame:
    """Load and inspect the dataset in a csv file"""
    df = pd.read_csv(file_path)
    print(f"General info for {file_path.split("/")[-1]}:\n")
    print(f"Columns: {df.columns.to_list()}\n")
    print(f"Data Types:\n{df.dtypes}\n")
    print(f"Shape: {df.shape}\n")
    print(f"Missing Values: {not df.notnull().any().any()}\n")
    print(f"Duplicated Rows: {df.duplicated().any()}\n")
    print(f"Summary Statictis:\n {df.describe()}\n")
    return df

# Define a function that optimize the memory usage
def opitimize_memory(df: pd.DataFrame) -> pd.DataFrame:
    """Optimize the memory usage of the DataFrame object"""
    # Optimize the integers and floats colums
    for col in df.select_dtypes(include=["int", "float"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="unsigned" if df[col].min() >= 0 else "integer")

    # Optimize object columns (strings), especially for categorical data
    for col in df.select_dtypes(include="object").columns:
        num_unique_values = df[col].nunique()
        num_total_values = len(df[col])
        if num_unique_values / num_total_values < 0.5:
            df[col] = df[col].astype("category")
    
    return df


# Load and inspect each dataset
datasets = {
    "links": "ml-latest-small/links.csv",
    "movies": "ml-latest-small/movies.csv",
    "ratings": "ml-latest-small/ratings.csv",
    "tags": "ml-latest-small/tags.csv"
}

dataframes = {name: load_and_inspect(path) for name, path in datasets.items()}

for name, df in dataframes.items():
    print(f"The memory usage of {name}: {df.memory_usage(deep=True).sum()/1024 ** 2:.2f}MB")
    opitimize_memory(df)
    print(f"The memory usage of {name} after optimizating: {df.memory_usage(deep=True).sum()/1024 ** 2:.2f}MB\n")