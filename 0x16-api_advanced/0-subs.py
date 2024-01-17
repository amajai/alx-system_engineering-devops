#!/usr/bin/python3
"""
Module for subreddit count api
"""
import requests


def number_of_subscribers(subreddit):
    """
    get number of subs from a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    res = requests.get(
        url,
        allow_redirects=False,
        headers={
            "User-Agent": "MyCustomUserAgent/1.0"
        }
    )
    if res.status_code == 200:
        data = res.json()["data"]["children"][0]["data"]
        return data['subreddit_subscribers']
    else:
        return 0
