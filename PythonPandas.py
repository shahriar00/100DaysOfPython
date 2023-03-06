import numpy as np
import pandas as pd

# Pandas is a python library...
# Pandas made data framing......

# mydata = {
#     'car':["volvo","vr","audy"],
#     'price':[222,444,555]
# }
# myvar = pd.DataFrame(mydata)
# print(myvar)

# A Pandas Series is like a column in a table.
# data = [1,3,5,6]
# mydata = pd.Series(data,index=["a","b","c","d"])
# print(mydata)
#
# data1 = {
#     "name":["Abir","Asik","Onik"],
#     "age":[32,22,55],
#     "address":["Dhaka","Rajshai","Sylhet"]
# }
# mydata1 = pd.DataFrame(data1,index=["name","age","address"])
# print(mydata1.loc["age"])

# A Pandas DataFrame is a 2 dimensional data structure like a 2 dimensional array, or a table with rows and columns.
# df = pd.read_csv('data.csv')
# print(df.to_string())
# print(df.head(10))

# df = pd.read_json('data.json')
# print(df.to_string())

# json_data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },}
# myjason=pd.DataFrame(json_data)
# print(myjason)

# Data Cleaning in Pandas.....

# Empty cells.......
# df = pd.read_csv('data.csv')
# x = df.dropna()

# x = df.dropna(inplace=True)
# print(x)

# df.fillna(140,inplace=True)
# df['Calories'].fillna(130,inplace=True)
# m = df['Calories'].mean()
# m = df['Calories'].median()
# m = df['Calories'].mode()[0]
# df['Calories'].fillna(m,inplace=True)
# print(df.to_string())

# Wrong formate Data....
# df['Date'] = pd.to_datetime(df['Date'])

# print(df.to_string())

# Wrong data.....
# df.loc[7,'Duration']=45
# print(df.to_string())

# for x in df.index:
#   if df.loc[x,"Duration"]>120:
#     df.drop(x,inplace=True)
# print(df.to_string())

# Removing duplicate data.....
# df.drop_duplicates(inplace=True)
# print(df.to_string())
