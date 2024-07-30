import os
import requests

def list_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=100"
    token = os.environ.get('COINGECKO_TOKEN')

    headers = {
        "accept": "application/json",
        "x-cg-api-key": token
    }

    response = requests.get(url, headers=headers)
    
    # Check if the response was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

    data = response.json()

    # Log the type and first few elements of the data to debug the structure
    # print(f"Data type: {type(data)}, First element: {data[0] if data else 'No data'}")

    filtered_data = []
    for coin in data:
        # Ensure coin is a dictionary
        if isinstance(coin, dict):
            filtered_coin = {
                "id": coin["id"],
                "symbol": coin["symbol"],
                "name": coin["name"],
                "image": coin["image"],
                "current_price": coin["current_price"],
                "market_cap": coin["market_cap"],
                "market_cap_rank": coin["market_cap_rank"],
                "price_change_percentage_24h": coin["price_change_percentage_24h"],
                "total_volume": coin["total_volume"],
                "high_24h": coin["high_24h"],
                "low_24h": coin["low_24h"],
            }
            filtered_data.append(filtered_coin)
        else:
            print(f"Unexpected data type: {type(coin)}")

    return filtered_data
