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


def get_info(id: str):
    url = f"https://api.coingecko.com/api/v3/coins/{id}?localization=false&tickers=false&community_data=false&developer_data=false&sparkline=false"
    token = os.environ.get('COINGECKO_TOKEN')

    headers = {
        "accept": "application/json",
        "x-cg-api-key": token
    }

    response = requests.get(url, headers=headers)
    
    # Check if the response was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

    coin = response.json()
    
    filtered_data = []
    filtered_coin = {
                "id": coin["id"],
                "symbol": coin["symbol"],
                "name": coin["name"],
                "categories": coin["categories"][0],
                "description": coin["description"]["en"],
                "homepage": coin["links"]["homepage"][0],
                "whitepaper": coin["links"]["whitepaper"],
                # "blockchain_site": coin["links"]["blockchain_site"],
                "official_forum_url": coin["links"]["official_forum_url"][0],
                "subreddit_url": coin["links"]["subreddit_url"],
                "repos_url": coin["links"]["repos_url"]["github"][0],
                "image": coin["image"]["small"],
                "market_cap_rank": coin["market_cap_rank"],
                "current_price": coin["market_data"]["current_price"]["usd"],
                "ath": coin["market_data"]["ath"]["usd"],
                "ath_change_percentage": coin["market_data"]["ath_change_percentage"]["usd"],
                "atl": coin["market_data"]["atl"]["usd"],
                "market_cap": coin["market_data"]["market_cap"]["usd"],
                "fully_diluted_valuation": coin["market_data"]["fully_diluted_valuation"]["usd"],
                "total_volume": coin["market_data"]["total_volume"]["usd"],
                "high_24h": coin["market_data"]["high_24h"]["usd"],
                "low_24h": coin["market_data"]["low_24h"]["usd"],
                "price_change_24h": coin["market_data"]["price_change_24h"],
                "price_change_percentage_24h": coin["market_data"]["price_change_percentage_24h"],
                "price_change_percentage_7d": coin["market_data"]["price_change_percentage_7d"],
                "market_cap_change_24h": coin["market_data"]["market_cap_change_24h"],
                "market_cap_change_percentage_24h": coin["market_data"]["market_cap_change_percentage_24h"],
                "price_change_percentage_1h_in_currency": coin["market_data"]["price_change_percentage_1h_in_currency"]["usd"],
                "price_change_percentage_24h_in_currency": coin["market_data"]["price_change_percentage_24h_in_currency"]["usd"],
                "market_cap_change_24h_in_currency": coin["market_data"]["market_cap_change_24h_in_currency"]["usd"],
                "total_supply": coin["market_data"]["total_supply"],
                "circulating_supply": coin["market_data"]["circulating_supply"],
                "max_supply": coin["market_data"]["max_supply"],
                "last_updated": coin["market_data"]["last_updated"]
    }

    filtered_data.append(filtered_coin)

    return filtered_data
