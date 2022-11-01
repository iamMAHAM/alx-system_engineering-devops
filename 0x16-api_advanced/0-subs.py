#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:iamMAHAMv1 (programmer)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    return (res.json().get("data").get('subscribers'))
