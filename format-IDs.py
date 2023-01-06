'''Note - this was written originally in
Jupyter Notebook and currently doesn't work in IDLE.
It does run in Anaconda Powershell.
'''

'''Sometimes I need to write UPDATE queries for an SQL database,
using the IN operator to reference specific ID numbers.
As each ID needs to be in single quotes, separated by a comma,
I wanted to try writing a script that could pull IDs from a file,
and then write the formatted IDs to another file as a way to help
prep data for an SQL query. e.g. 12345 to '12345',
'''


import pandas as pd

print()

#the IDs needed are in column A of this Excel file
df_pubs = pd.read_excel('2021_pubs.xlsx')

print()

#when writing this script, I used these functions along the way
#to see how things were looking.
df_pubs.shape
df_pubs.dtypes
df_pubs.info()

print()
df_ids = df_pubs[["ID"]]
print('___________________')
print()

df_ids.head()

print(f"'{df_ids}'")
print()
print('See ids_formatted.csv for full list of formatted ids.')
print()

df_pubs['ids_formatted'] = "'" + df_pubs['ID'].astype(str) + "',"

df_pubs.head()

df_ids_formatted = df_pubs['ids_formatted'] = "'" + df_pubs['ID'].astype(str) + "',"


df_ids_formatted.head()


#to run this on a different machine, change the folder path accordingly.
df_ids_formatted.to_csv('C:/Users/fifes/Desktop/ForGitHub/ids_formatted.csv', index=False)


