import redis

try:
    # Try to connect to the Redis server
    r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    
    # Test the connection
    response = r.ping()
    print("Connected to Redis:", response)
except Exception as e:
    print("Error connecting to Redis:", e)

