import pandas as pd
from data_loading import dataframes

df = dataframes["ratings"]

print(df["userId"] == 1)