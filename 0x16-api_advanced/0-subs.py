#!/usr/bin/python3
"""import statement """
import requests


def number_of_subscribers(subreddit):
    """Define the URL for the Reddit API endpoint"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    """Send a GET request to the Reddit API"""
    try:
        response = requests.get(url, headers)
        response.raise_for_status()
        data = response.json()

        subscribers = data['data']['subscribers']
        return subscribers

    except requests.RequestException as e:
        pass
        return 0


if __name__ == "__main__":
    subreddit = "python"  # Replace with your subreddit
    print(f"Number of subscribers: {number_of_subscribers(subreddit)}")
