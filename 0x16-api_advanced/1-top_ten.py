import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for post in children:
            print(post['data']['title'])
    else:
        print("Error: Unable to fetch data from Reddit API")

# Test the function
if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)
