import json
from fastapi import FastAPI
from api.candlestick_pattern.analysis import get_analysis
from api.youtube.analysis import get_video_analysis

app = FastAPI()

@app.get("/")
async def pattern_recognition():
    data = get_analysis('bitcoin', 1, 'usd')
    response = json.loads(data.to_json(orient='records'))
    return response

async def youtube_video_analysis():
    data = get_video_analysis('bitcoin news|bitcoin cryptocurrency prediction|bitcoin cryptocurrency news')
    response = json.loads(data.to_json(orient='records'))
    return response