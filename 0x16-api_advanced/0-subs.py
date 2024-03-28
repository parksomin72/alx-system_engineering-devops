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
if __name__ == '__main__':
    subreddit = sys.argv[1] if len(sys.argv) > 1 else None
    if subreddit:
        subscribers = number_of_subscribers(subreddit)
        if subscribers != 0:
            print("OK")
        else:
            print("Invalid subreddit or error occurred.")
    else:
        print("Please pass an argument for the subreddit to search.")
