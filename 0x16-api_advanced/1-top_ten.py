import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json().get('data')
            if data:
                children = data.get('children')
                if children:
                    for post in children:
                        print(post.get('data').get('title'))
        except Exception as e:
            print("Error parsing JSON: {}".format(e))
    else:
        print("Request failed with status code {}".format(response.status_code))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
