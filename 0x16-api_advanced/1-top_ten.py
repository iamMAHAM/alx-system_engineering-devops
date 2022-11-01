#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:iamMAHAMv1 (programmer)"
    }
    res = requests.get(url, headers=headers, params={'limit': 10},
                       allow_redirects=False)
    if res.status_code == 404:
        return 0

    posts = res.json().get('data').get('children')
    [print(p.get('data').get('title')) for p in posts]
