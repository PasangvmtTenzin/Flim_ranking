import pandas as pd 

file_path = 'cleaned_data/merged_cinematic_data.csv'

df = pd.read_csv(file_path)

print(df.isnull().sum())
print(df.head(5))
print(df.info())