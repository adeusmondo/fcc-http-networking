import asyncio
import json
import math
import random
import urllib.request

from types import SimpleNamespace


def get_settings():
    return {
        'data': None,
        'headers': {'X-API-Key': API_KEY, 'Content-Type': 'application/json'},
        'origin_req_host': None,
        'unverifiable': None,
        'method': 'GET'
    }

def get_url():
    return 'https://api.boot.dev/v1/courses_rest_api/learn-http/items'

def generate_key():
    characters = 'ABCDEF0123456789'
    result = ''
    for _ in range(16):
        result += characters[math.floor(random.uniform(0, 1) * len(characters))]
    return result

def log_items(items):
    for item in items:
        print(SimpleNamespace(**item).name)

API_KEY = generate_key()

# Do not touch the lines above

async def main():
    url = get_url()
    settings = get_settings()

    loop = asyncio.get_event_loop()
    urllib_request_future = loop.run_in_executor(None, urllib.request.Request, url, *settings.values())
    response = urllib_request_future
    with urllib.request.urlopen(response) as f:
        response_data = json.loads(f.read().decode('utf-8'))
    
    log_items(response_data)
    
# Don't touch below this line

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
