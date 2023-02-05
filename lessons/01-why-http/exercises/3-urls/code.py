import asyncio
import json
import math
import random
import urllib.request

from types import SimpleNamespace

API_KEY = None
ITEM_URL = 'https://api.boot.dev/v1/courses_rest_api/learn-http/items'

def generate_key():
    characters = 'ABCDEF0123456789'
    result = ''
    for _ in range(16):
        result += characters[math.floor(random.uniform(0, 1) * len(characters))]
    return result

def log_items(items):
    for item in items:
        print(SimpleNamespace(**item).name)

async def get_data(url=''):
    loop = asyncio.get_event_loop()
    urllib_request_future = loop.run_in_executor(None, urllib.request.Request, url, None,
                                                 {'X-API-Key': API_KEY, 'Content-Type': 'application/json'},
                                                 None, None, 'GET')
    urllib_request = await urllib_request_future
    with urllib.request.urlopen(urllib_request) as f:
        data = json.loads(f.read().decode('utf-8'))
    return data 

API_KEY = generate_key()

async def main():
    items = await get_data()
    log_items(items)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())





