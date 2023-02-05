import asyncio
import json
import urllib.request

DOMAIN = 'api.boot.dev'

# Do not touch the lines above

async def fetch_ip_address(domain: str):
    url = f'https://cloudflare-dns.com/dns-query?name={domain}&type=A'
    loop = asyncio.get_event_loop()
    urllib_request_future = loop.run_in_executor(None, urllib.request.Request, url,
                                                 None, {'accept': 'application/dns-json'}, None, None, 'GET')
    resp = await urllib_request_future
    with urllib.request.urlopen(resp) as f:
        resp_object = json.loads(f.read().decode('utf-8'))

    return resp_object.get('Answer', [{}])[0].get('data')
    
# Don't touch below this line

async def main():
    ip_address = await fetch_ip_address(DOMAIN)
    if (ip_address is None):
        print('something went wrong in fetchIPAddress')
    else:
        print(f'found IP address for domain {DOMAIN}: {ip_address}')

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
