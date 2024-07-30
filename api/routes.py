import json
from fastapi import FastAPI
from api.Newsfeed import get_specific_news, top_news
from api.candlestick_pattern.analysis import get_analysis
from api.youtube.analysis import get_video_analysis
from api.Coins import list_coins

app = FastAPI()

@app.get("/")
async def pattern_recognition():
    data = get_analysis('bitcoin', 1, 'usd')
    response = json.loads(data.to_json(orient='records'))
    return response

@app.get("/youtube")
async def youtube_video_analysis():
    data = get_video_analysis('bitcoin news') # |bitcoin cryptocurrency prediction|bitcoin cryptocurrency news
    # response = json.loads(data.to_json(orient='records'))
    return data

@app.get("/allcoins")
async def get_all_coins():
    data = list_coins()
    return data

@app.get("/top/news")
async def get_news():
    data = top_news()
    return data

@app.get("/news/{coin}")
async def get_crypto_news(coin: str):
    data = get_specific_news(coin)
    return data