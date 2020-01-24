import cx_Oracle
import pandas as pd

dsn_tns = cx_Oracle.makedsn('gpocbs1o.ced.it', '1527', service_name='gpocbs1o') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'proc_dau', password='proc_dau', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

df = pd.read_sql_query("SELECT * FROM mazzette_batch", conn)
print(df)

# fornisce info sul dataframe
df.info()
# numero di righe e colonne
print(df.shape)

df.to_csv('c:\\temp\\mazzette_batch.csv')
df.to_json('c:\\temp\\mazzette_batch.json')

print(df.isnull().sum())