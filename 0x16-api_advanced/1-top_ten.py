#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.1'}  # Reddit API requires a User-Agent header

    response = requests.get(url, headers=headers)
    
    # If subreddit is invalid or not found, print None
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    posts = data['data']['children']
    
    for post in posts:
        print(post['data']['title'])

if __name__ == "__main__":
    # Example usage
    top_ten("programming")
