#!/usr/bin/python3
"""
0-subs: A script to retrieve the number of subscribers
for a given subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0

if __name__ == '__main__':
    number_of_subscribers = number_of_subscribers(input("Enter subreddit: "))
    print(number_of_subscribers)
