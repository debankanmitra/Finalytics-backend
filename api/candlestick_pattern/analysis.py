import datetime
import os
import requests
import pandas as pd
from api.candlestick_pattern import patterns


def convert_to_datetime(timestamp):
  # Convert milliseconds to seconds
  timestamp_seconds = timestamp / 1000

  # Convert Unix timestamp to datetime
  dt_object = datetime.datetime.fromtimestamp(timestamp_seconds)

  # Print the datetime object
  return dt_object

def change_DataFrame(data):
    df = pd.DataFrame(data)
    df.columns = ["timestamp","Open", "High", "Low", "Close"]
    df['Pattern']=None

    # Apply the function to the timestamp column
    df['timestamp'] = df['timestamp'].apply(convert_to_datetime)

    return df

def get_analysis(ticker, days, currency):
    url = f"https://api.coingecko.com/api/v3/coins/{ticker}/ohlc?vs_currency={currency}&days={days}&precision=0"

    token = os.environ.get('COINGECKO_TOKEN')

    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    new_data = change_DataFrame(data)
    new_data_with_pattern=patterns.recognized_pattern(new_data)
    
    return new_data_with_pattern