from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

# Set DEVELOPER_KEY to the API key value
YOUTUBE_DATA_API_KEY = os.environ.get('YOUTUBE_DATA_API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search_videos(query):
    # Create a Youtube service object
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_DATA_API_KEY)
    
    # Call the search.list method to retrieve results matching the specified query term.
    search_parameters = {
        "q": query,
        "part":'id,snippet',
        'type':'video',
        'maxResults':5
    };
    search_response = youtube.search().list(**search_parameters).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            dataObj={
                'kind':search_result['id']['kind'],
                'id':search_result['id']['videoId'],
                'url':'https://www.youtube.com/watch?v='+search_result['id']['videoId'],
                'channelId':search_result['snippet']['channelId'],
                'title':search_result['snippet']['title'],
                'description':search_result['snippet']['description'],
                'channelTitle':search_result['snippet']['channelTitle'],
                'publishTime':search_result['snippet']['publishTime']
            }
            videos.append(dataObj)

    return videos

print(search_videos('bitcoin'))