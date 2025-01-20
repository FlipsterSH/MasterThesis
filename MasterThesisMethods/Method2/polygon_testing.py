import requests
import pandas as pd


API_KEY = "xAe4nDCpgV8ruHpsMByY6duyQ24yFDgR"

GET_BTC_URL = "https://api.polygon.io/v2/aggs/ticker/X:BTCUSD/range/1/hour/2020-01-01/2025-10-10?adjusted=true&sort=asc&limit=5000&apiKey=rsFLH9sX79BS1vAWQmsoZNOsotm3D0Aq"



def make_api_call(url):
    """
    Makes a GET request to the specified URL and returns the response content.

    :param url: The endpoint to which the GET request is sent.
    :type url: str
    :return: The response content from the API call.
    :rtype: dict or str
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError if the response was unsuccessful
        return response.json()       # If the API returns JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API call: {e}")
        return None
    

def join_dataframes_columnwise(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Join two DataFrames of the same structure columnwise (side by side).

    :param df1: First DataFrame.
    :param df2: Second DataFrame.
    :return: A new DataFrame with columns from df1 followed by columns from df2.
    """
    # Concatenate the DataFrames along the columns (axis=1).
    joined_df = pd.concat([df1, df2], axis=1)
    return joined_df
    

resp = make_api_call(GET_BTC_URL)
dataframe1 = pd.DataFrame(resp["results"])
print(dataframe1)

next = resp["next_url"].split("?")
next_url = next[0] + "?apiKey=" + API_KEY
print(next)
resp2 = make_api_call(next_url)
dataframe2 = pd.DataFrame(resp2["results"])
print(dataframe2)