import pandas as pd

# Read the CSV data
csv1 = 'outputIQA.csv'
csv2 = 'outputTREES.csv'

df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

# Merge the DataFrames on the common column (e.g., 'date')
merged_df = pd.merge(df1, df2, on='date')

# Select only numeric columns for correlation calculation
numeric_columns = merged_df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = merged_df[numeric_columns].corr()

print(correlation_matrix)