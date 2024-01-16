#!/usr/bin/python3
"""
Module for subreddit count api
"""
from json import JSONDecodeError
import requests


def number_of_subscribers(subreddit):
    try:
        url = f"https://www.reddit.com/r/{subreddit}/new.json"
        res = requests.get(url)
        subreddit_obj = res.json()["data"]["children"][0]["data"]
        count = subreddit_obj["subreddit_subscribers"]
        return count
    except JSONDecodeError:
        return 0
