import pandas as pd

""" Loading data from a file
    Pandas is capable of read any document file
    Such as xls, csv, html, json
"""

df = pd.read_csv("file.csv")


""" Even read a txt as a csv file """

df_txt = pd.read_csv("file.txt", delimiter= '\t')

""" Getting the first n or last n rows of the dataFrame """

tail = df.tail(3)
head = df.head(4)

""" Getting a common value from the dataFrame """

headers = df.columns

column = df['column_name']['slice partition']

columns = df[['column_name', 'another_column_name']]

row = df.iloc['index']

row = df.iloc['slice partition']

cell = df.iloc['column_index', 'row_index']

""" Iterate through all the rows """

for index, row in df.iterrows():
    print(index, row['possible_column_name'])