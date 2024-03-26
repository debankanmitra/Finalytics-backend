import time
from api.youtube.summarizer import get_summary, llm_summarize
from api.youtube.search import search_videos

def get_video_analysis(keywords):
    analysis = []

    # get youtube videos info like url, title, description etc
    videos=search_videos(keywords)

    for index, video in enumerate(videos, start=1):
        summary=get_summary(video['url'])
        record = {
            f'summary {index}': summary,
        }
        analysis.append(record)
        
        # sleep for 3 seconds to avoid hitting rate limit
        time.sleep(3)

    llm_analysis = llm_summarize(analysis)
    analysis.append({'LLM Analysis': llm_analysis})
    
    return analysis

# get_video_analysis('bitcoin news|bitcoin cryptocurrency prediction|bitcoin cryptocurrency news')
    