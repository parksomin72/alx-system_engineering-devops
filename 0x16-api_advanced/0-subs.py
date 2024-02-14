import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
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
    result_existing = number_of_subscribers("programming")
    print(result_existing)  # Output: OK

    # Non-existing subreddit
    print("Output: non-existing subreddit")
    result_non_existing = number_of_subscribers("this_is_a_fake_subreddit")
    print(result_non_existing)  # Output: OK
