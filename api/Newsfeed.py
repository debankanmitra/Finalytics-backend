from datetime import datetime, timedelta
import re
from newsapi import NewsApiClient


def top_news():
    newsapi = NewsApiClient(api_key="7a28dcade6a641a996ace652b8d92aac")


    # Calculate the date 7 days before today
    seven_days_ago = datetime.today() - timedelta(days=7)

    # Format the date to YYYY-MM-DD
    date= seven_days_ago.strftime('%Y-%m-%d')

    # /v2/everything
    all_articles = newsapi.get_everything(
        q="cryptocurrency",
        from_param=date,
        language="en",
        sort_by="relevancy",
        page_size=6,
    )
    articles = []

    for article in all_articles["articles"]:
        if isinstance(article, dict):
            # Use regex to remove parts within []
            content = re.sub(r'\[.*?\]', '', article.get("content", ""))
            
            filtered_article = {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "urlToImage": article["urlToImage"],
                "publishedAt": article["publishedAt"],
                "content": content,
            }
            articles.append(filtered_article)
    return articles


def get_specific_news(coin: str):
    newsapi = NewsApiClient(api_key="7a28dcade6a641a996ace652b8d92aac")
    all_articles = newsapi.get_everything(
        q=coin+" cryptocurrency",
        language="en",
        sort_by="relevancy",
        page_size=4,
    )
    articles = []

    for article in all_articles["articles"]:
        if isinstance(article, dict):
            # Use regex to remove parts within []
            content = re.sub(r'\[.*?\]', '', article.get("content", ""))
            
            filtered_article = {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "urlToImage": article["urlToImage"],
                "publishedAt": article["publishedAt"],
                "content": content,
            }
            articles.append(filtered_article)
    return articles