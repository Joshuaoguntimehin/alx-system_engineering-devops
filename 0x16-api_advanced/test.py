#!/usr/bin/python3
"""Import statement"""


import requests


def number_of_subscribers(subreddit):
    """Fetch the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.raise_for_status()
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0


if __name__ == "__main__":
    subreddit = "python"  # Replace with your subreddit
    print(f"Number of subscribers: {number_of_subscribers(subreddit)}")
