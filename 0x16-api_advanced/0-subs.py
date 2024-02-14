#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers. Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.1'}  # Reddit API requires a User-Agent header

    response = requests.get(url, headers=headers)
    
    # If subreddit is invalid or not found, return 0
    if response.status_code != 200:
        return 0
    
    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers

if __name__ == "__main__":
    # Example usage
    print(number_of_subscribers("programming"))
    print(number_of_subscribers("this_is_a_fake_subreddit"))
