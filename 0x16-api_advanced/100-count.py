#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    if not data:
        return

    children = data.get('children')
    if not children:
        return

    for post in children:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            if word.lower() in title:
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    after = data.get('after')
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
       print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
       print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
