#!/usr/bin/python3
"""Function to query subscribers on a give Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Linux:0x16.api.advance:v1.0.0 (by /u/parksomin72)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
