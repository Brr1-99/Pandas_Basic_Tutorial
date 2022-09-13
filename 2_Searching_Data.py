import pandas as pd

df = pd.read_csv("file.csv")

""" Looking for specific condition """

condition = df.loc[df['condition'] == "value"]

""" Get most common stadistical values """

stats = df.describe()

""" Sorting values """

sorted = df.sort_values(['column_name', 'another_column_name'], ascending=[1, 0])