#!/usr/bin/env python3
"""import statement"""
import uuid
import redis

class Cache:
    def __init__(self, redis_host='localhost', redis_port=6379):
        # Initialize Redis connection
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    def store(self, data):
        # Generate a random UUID as the key
        key = str(uuid.uuid4())

        # Store the data in Redis
        self.redis_client.set(key, data)

        # Return the generated key
        return key
