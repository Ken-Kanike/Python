import pandas as pd 

# 5 commonly used pandas functions
# 1. read_csv() - Read a CSV file into a DataFrame
df = pd.read_csv('example.csv')

# 2. head() - Display the first few rows of a DataFrame
print(df.head())

# 3. describe() - Generate descriptive statistics of a DataFrame
print(df.describe())

# 4. groupby() - Group DataFrame using a mapper or by a Series of columns
grouped = df.groupby('column_name')

# 5. to_datetime() - Convert argument to datetime
df['date_column'] = pd.to_datetime(df['date_column'])