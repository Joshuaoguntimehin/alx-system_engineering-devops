#!/usr/bin/python3
"""Import statement"""


import requests


def top_ten(subreddit):
    """Fetch the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.raise_for_status()
        data = response.json()

        post = data.get('data', {}).get('children', [])
        for post in post[:10]:
            title = post.get('data', {}).get('title', 'No Title')
            print(title)
    else:
        print("None")
        return


if __name__ == "__main__":
    subreddit = "python"  # Replace with your subreddit
    top_ten(subreddit)
