#!/usr/bin/python3
"""import statement """
import requests


def number_of_subscribers(subreddit):
    """Define the URL for the Reddit API endpoint"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    """Send a GET request to the Reddit API"""

    response = requests.get(url, headers, allow_redirects=False)
    if response.status_code == 200:
        response.raise_for_status()
        data = response.json()
        return data.get('data', {}).get('subscriber', 0)
    else:
        return 0
