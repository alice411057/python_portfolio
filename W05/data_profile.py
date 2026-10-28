import pandas as pd

df = pd.read_csv('messy_students.csv')

print(df.head(20))

df = df.drop_duplicates()
df['name'] = df['name'].str.strip()

print(df.head(20))
