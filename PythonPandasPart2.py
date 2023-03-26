# Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

# new_df = df.dropna()

# df.dropna(inplace=True)
# df.fillna(122,inplace=True)

# x = df["Calories"].mean()
# x = df["Calories"].median()
# x = df["Calories"].mode()
# df["Calories"].fillna(x, inplace = True)

# print(df.to_string())

# Data of Wrong Format

# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())

# Wrong Data
# df.loc[7, 'Duration'] = 45
# for x in df.index:
# if df.loc[x, "Duration"] > 120:
# df.loc[x, "Duration"] = 120

# Discovering Duplicates
# df.duplicated()
# df.drop_duplicates(inplace=True)
