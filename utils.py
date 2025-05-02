import requests
from bs4 import BeautifulSoup
from datetime import datetime

def generate_rss(username):
    url = f"https://nitter.net/{username}"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, 'html.parser')
    tweets = soup.select(".timeline-item")

    items = ""
    for tweet in tweets[:5]:
        content = tweet.select_one(".tweet-content").text.strip()
        link = "https://nitter.net" + tweet.select_one("a.tweet-date")["href"]
        pub_date = tweet.select_one("a.tweet-date span")["title"]
        items += f"""
        <item>
            <title>{content[:50]}...</title>
            <description>{content}</description>
            <link>{link}</link>
            <pubDate>{pub_date}</pubDate>
        </item>
        """

    rss = f"""<?xml version="1.0"?>
    <rss version="2.0">
    <channel>
        <title>Twitter feed for {username}</title>
        <link>https://nitter.net/{username}</link>
        <description>Flux RSS personnalisé</description>
        {items}
    </channel>
    </rss>
    """
    return rss
