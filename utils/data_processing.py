import pandas as pd

def filter_date(df, start_date, end_date, date_column="date"):
    df[date_column] = pd.to_datetime(df[date_column])
    return df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]
