# Importing the necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Define a function to load and inspect a dateset
def load_and_inspect(file_path: str) -> pd.DataFrame:
    """Load and inspect the dataset in a csv file"""
    df = pd.read_csv(file_path)
    print(f"General info for {file_path.split("/")[-1]}:\n")
    print(f"Columns: {df.columns.to_list()}")
    print(f"Data Types:\n{df.dtypes}\n")
    print(f"Shape: {df.shape}\n")
    print(f"Missing Values: {not df.notnull().any().any()}\n")
    print(f"Duplicated Rows: {df.duplicated().any()}\n")
    print(f"Summary Statictis:\n {df.describe()}\n")
    return df

# Load and inspect each dataset
datasets = {
    "links": "ml-latest-small/links.csv",
    "movies": "ml-latest-small/movies.csv",
    "ratings": "ml-latest-small/ratings.csv",
    "tags": "ml-latest-small/tags.csv"
}

dataframe = {name: load_and_inspect(path) for name, path in datasets.items()}