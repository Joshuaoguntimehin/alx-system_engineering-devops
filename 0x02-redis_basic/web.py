#!/usr/bin/env python3
"""import statement"""
import requests
import time
from functools import wraps

# Dictionary to store cached results
cache = {}

def cache_decorator(expiration_time: int):
    def decorator(func):
        @wraps(func)
        def wrapper(url: str):
            current_time = time.time()
            cache_key = f'count:{url}'
            # Check if URL is cached
            if cache_key in cache:
                cached_value, timestamp = cache[cache_key]
                if current_time - timestamp < expiration_time:
                    print(f"Using cached value for {url}")
                    return cached_value
            
            # Call the original function
            result = func(url)
            # Cache the result with the current timestamp
            cache[cache_key] = (result, current_time)
            print(f"Caching new value for {url}")
            return result
        return wrapper
    return decorator

@cache_decorator(expiration_time=10)
def get_page(url: str) -> str:
    """Fetch HTML content of the given URL."""
    response = requests.get(url)
    return response.text
