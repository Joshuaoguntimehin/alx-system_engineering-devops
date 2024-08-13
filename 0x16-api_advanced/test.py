#!/usr/bin/python3
"""Import statement"""


import requests


def recurse(subreddit, hot_list=[]):
    if title is None:
        titles = []
    
    
    """Fetch the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {}
    if after:
        params['after'] = after
        
     
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        posts = data.get('data', {}).get('children', [])
        if not posts:
            return titles if titles else None
        
        for post in posts:
            title = post.get('data', {}).get('title', 'No Title')
            titles.append(title)
        
        # Check for more posts
        after = data.get('data', {}).get('after', None)
        if after:
            return recurse(subreddit, after, titles)
        else:
            return titles
    
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    subreddit = "python"  # Replace with your subreddit
    all_titles = recurse(subreddit)
    if all_titles:
        for title in all_titles:
            print(title)
    else:
        print("No results found.")
    