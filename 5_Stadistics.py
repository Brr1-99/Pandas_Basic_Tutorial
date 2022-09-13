import pandas as pd

df = pd.read_csv("file.csv")

""" GroupBy mean, sum, count """

df.groupby(['column_name']).mean().sort_values('another_column_name', ascending=False)

df.groupby(['column_name', 'another_column_name']).sum()