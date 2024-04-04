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
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json().get("data")
        if data is not None:
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.HTTPError as e:
        print("HTTP Error: {} - {}".format(e.response.status_code, e.response.reason))
    except requests.RequestException as e:
        print("Request Exception: {}".format(e))
    except ValueError as e:
        print("JSON Decoding Error: {}".format(e))
    return 0  # Return 0 for any encountered errors

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        print("{:d}".format(subscribers))
