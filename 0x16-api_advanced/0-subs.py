#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User_Agent": "Linux:0x16.api.advance:v1.0.0 (by /u/parksomin72)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    try:
        data = response.json().get("data")
        if data is not None:
            return data.get("subscribers", 0)
        else:
            return 0
    except ValueError:
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
