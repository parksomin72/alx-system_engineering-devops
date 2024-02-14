mport requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

# Example usage
if __name__ == "__main__":
    # Existing subreddit
    print("Output: existing subreddit")
    print(number_of_subscribers("programming"))  # Output: OK

    # Non-existing subreddit
    print("Output: non-existing subreddit")
    print(number_of_subscribers("this_is_a_fake_subreddit"))  # Output: OK
