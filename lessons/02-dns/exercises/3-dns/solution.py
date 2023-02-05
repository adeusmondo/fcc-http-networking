from urllib.parse import urlparse

BOOT_DEV_URL = 'https://boot.dev/learn/learn-python'

# Do not touch the lines above

def get_domain_name_from_url(url):
    url_parsed = urlparse(url)
    return url_parsed.netloc

# Don't touch below this line

def main():
    domain_name = get_domain_name_from_url(BOOT_DEV_URL)
    print(f'The domain name for {BOOT_DEV_URL} is {domain_name}')

if __name__ == '__main__':
    main()
