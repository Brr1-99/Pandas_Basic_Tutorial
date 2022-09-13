import pandas as pd
import math

df = pd.read_csv("file.csv")

""" Creating a new column """

df['new_column_name'] = df['column_1'] + df['column_2']

df['new_column_name'] = df.iloc[:, "n":"m"].sum(axis=1)

""" Deleting a column """

df.drop(columns=['column'])

""" Rearranging columns """

cols = list(df.columns)

df = df[cols["n":"m"] + cols["p", "q"]]

""" Conditional changes for the same or another column """

df.loc[df['column'] == 'value', 'column'] = 'new_value'

df.loc[df['column'] > 'value', ['column_1', 'column_2']] = ['new_value_1', 'new_value_2']

""" Changes based on an applied funciton """

df['column'].apply(lambda x: x + 3, axis=0)
df['column'].apply(math.sqrt, index= "Square root")

""" Saving our changed dataFrame 
    Pandas is capable of saving it as any document file
    Same ones as it is capable of reading
"""

df.to_csv("new_file.csv", index=False)
df.to_csv("new_file.txt", index=False, sep="\t")
df.to_excel("new_file.xlsx", index=False)