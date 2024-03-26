from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import os

# Set DEVELOPER_KEY to the API key value
YOUTUBE_DATA_API_KEY = os.environ.get('YOUTUBE_DATA_API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def uploaded_thisweek():
    this_week = datetime.now() - timedelta(days=7)
    this_week = datetime.strftime(this_week, '%Y-%m-%dT%H:%M:%S')+'Z' # we can use isoformat() as well
    return this_week

def search_videos(query):
    # Create a Youtube service object
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_DATA_API_KEY)

    uploaded_date=uploaded_thisweek()

    # Call the search.list method to retrieve results matching the specified query term.
    search_parameters = {
        "q": query,
        "part":'id,snippet', # contentDetails,statistics - needs proper permission to use
        'type':'video',
        'relevanceLanguage':'en',
        'safeSearch':'moderate',
        'videoDuration':'medium',
        'publishedAfter':uploaded_date,
        'maxResults':3
    };
    search_response = youtube.search().list(**search_parameters).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video' and search_result['snippet']['liveBroadcastContent'] == 'none':
            video_data={
                'kind':search_result['id']['kind'],
                'id':search_result['id']['videoId'],
                'url':'https://www.youtube.com/watch?v='+search_result['id']['videoId'],
                'channelId':search_result['snippet']['channelId'],
                'title':search_result['snippet']['title'],
                'description':search_result['snippet']['description'],
                'channelTitle':search_result['snippet']['channelTitle'],
                'publishTime':search_result['snippet']['publishTime']
            }
            videos.append(video_data)

    return videos

# print(search_videos('bitcoin news|bitcoin cryptocurrency prediction|bitcoin cryptocurrency news'))