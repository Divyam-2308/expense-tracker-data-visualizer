import pandas as pd
from datetime import date, timedelta

def filter_by_date(df, start_date=None, end_date=None):
    """Filter expenses between two dates."""
    df["Date"] = pd.to_datetime(df["Date"])

    if not start_date:
        start_date = df["Date"].min()
    if not end_date:
        end_date = df["Date"].max()

    mask = (df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))
    return df.loc[mask]