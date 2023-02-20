import pandas as pd
import sqlite3

df = pd.read_csv("/mnt/c/Users/ejunior/Documents/projects/azure-data-engineer/kc_house_data.csv")

df["date"] = pd.to_datetime(df["date"])


