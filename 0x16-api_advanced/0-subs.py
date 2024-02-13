import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Custom User-Agent header to prevent Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

# Test the function
if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    print(number_of_subscribers(subreddit))
