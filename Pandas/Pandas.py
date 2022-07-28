import pandas as pd
import numpy as np

# df = pd.read_csv("iris.csv")
# df.head()

# #print(df.head(10))
# #print(df.tail(10))

# filename = "lsg_stats.xlsx"
# xls = pd.ExcelFile(filename)
# xls.sheet_names

 
# for sheet in xls.sheet_names:
#     dfs = pd.read_excel(filename, sheet_name=sheet)
#     print(dfs.head())


df = pd.read_excel("lsg_stats.xlsx", sheet_name="2021q3")

# print(df2)

#  for column in df2.columns:
#     print(column)

new_cols = list(df.columns)
new_cols[0] = "Suburb"
new_cols[1] = "City"
new_df = df[new_cols]
# print(new_df.head())

df["Index"] = [i for i in range(len(df))]
df["Country"] = "USA"

print(df.head())


