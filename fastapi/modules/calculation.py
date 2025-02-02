import pandas as pd


def calculate_correlation(csv1, csv2):
    # Read the CSV data
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    # Merge the DataFrames on the common column (e.g., 'date')
    merged_df = pd.merge(df1, df2, on='date')

    # Select only numeric columns for correlation calculation
    numeric_columns = merged_df.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = merged_df[numeric_columns].corr()

    return correlation_matrix
