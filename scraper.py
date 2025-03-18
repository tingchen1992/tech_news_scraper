import feedparser
from datetime import datetime

RSS_URL = "https://techcrunch.com/feed/"


def get_techcrunch_news():
    feed = feedparser.parse(RSS_URL)
    news_items = []

    for entry in feed.entries:
        news_items.append(
            {"title": entry.title, "link": entry.link, "published": entry.published}
        )

    return news_items


if __name__ == "__main__":
    news = get_techcrunch_news()
    print("抓取的新聞:")
    print(news)  
