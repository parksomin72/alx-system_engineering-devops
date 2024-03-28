#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /u/parksomin72)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            for child in children:
                title = child.get("data").get("title")
                print(title)
        else:
            print("No posts found.")
    else:
        print("Error fetching posts.")

if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)
