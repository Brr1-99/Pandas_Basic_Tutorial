import pandas as pd
import re

df = pd.read_csv("file.csv")

""" Filter the data by multiple inclusive conditions """

df.loc[(df['column_1'] == 'value_1') & (df['column_2'] == 'value_2')]

new_df = df.loc[(df['column_1'] <= 'value_1') | (df['column_2'] > 'value_2')]

""" Reset the index when creating a dataFrame from filtered data """

new_df = new_df.reset_index(drop=True)

""" Reseting the index without creating a new variable """

new_df.reset_index(drop=True, inplace=True)

""" Filtering the data by a string expresion """

df.loc[df['column'].str.contains('string')]

""" Getting the data which does not contain the string """

df.loc[~df['column'].str.contains('string')]

""" Filtering the data with a regex espression """

df.loc[df['column'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

""" The same search can be done with pd.query """

df.query('column' > 'another_column')