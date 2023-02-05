import asyncio
import json
import math
import random
import urllib.request

from types import SimpleNamespace


# Do not touch the lines above

BOOT_DEV_API_DOMAIN = 'api.boot.dev'

# Don't touch below this line

API_KEY = None

def generate_key():
    characters = 'ABCDEF0123456789'
    result = ''
    for _ in range(16):
        result += characters[math.floor(random.uniform(0, 1) * len(characters))]
    return result

def log_items(items):
    for item in items:
        print(SimpleNamespace(**item).name)

async def get_item_data(domain=''):
    url = f'https://{domain}/v1/courses_rest_api/learn-http/items'
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
    items = await get_item_data(BOOT_DEV_API_DOMAIN)
    log_items(items)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
