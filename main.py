# Importing the necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""Convert each csv file to a DataFrame and retrieve its general information about it"""

# links.csv info

df_links = pd.read_csv("ml-latest-small/links.csv")

print("General Info For links.csv: \n")
print(f"The row labels of links.csv: {df_links.index}.\n") # We could use df_links.axes to get both row and colums labels
print(f"The colum labels of links.csv: {df_links.columns}.\n")
print(f"The data types in links.csv: {df_links.dtypes}.\n")
print(f"The number of axes of links.csv: {df_links.ndim}.\n")
print(f"The size of links.csv: {df_links.size}.\n")
print(f"The shape of links.csv: {df_links.shape}.\n") # We could get the shape by multiplying the lenght of rows labes and columns labes


# movies.csv info

df_movies = pd.read_csv("ml-latest-small/movies.csv")

print("General Info For movies.csv: \n")
print(f"The row labels of links.csv: {df_movies.index}.\n")
print(f"The colum labels of links.csv: {df_movies.columns}.\n")
print(f"The data types in links.csv: {df_movies.dtypes}.\n")
print(f"The number of axes of links.csv: {df_movies.ndim}.\n")
print(f"The size of links.csv: {df_movies.size}.\n")
print(f"The shape of links.csv: {df_movies.shape}.\n")


# ratings.csv info

df_ratings = pd.read_csv("ml-latest-small/ratings.csv")

print("General Info For ratings.csv: \n")
print(f"The row labels of links.csv: {df_ratings.index}.\n")
print(f"The colum labels of links.csv: {df_ratings.columns}.\n")
print(f"The data types in links.csv: {df_ratings.dtypes}.\n")
print(f"The number of axes of links.csv: {df_ratings.ndim}.\n")
print(f"The size of links.csv: {df_ratings.size}.\n")
print(f"The shape of links.csv: {df_ratings.shape}.\n")


# tags.csv info

df_tags = pd.read_csv("ml-latest-small/tags.csv")

print("General Info For ratings.csv: \n")
print(f"The row labels of links.csv: {df_tags.index}.\n")
print(f"The colum labels of links.csv: {df_tags.columns}.\n")
print(f"The data types in links.csv: {df_tags.dtypes}.\n")
print(f"The number of axes of links.csv: {df_tags.ndim}.\n")
print(f"The size of links.csv: {df_tags.size}.\n")
print(f"The shape of links.csv: {df_tags.shape}.\n")