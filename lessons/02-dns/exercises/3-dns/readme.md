# DNS

As we discussed, the "domain name" or "hostname" is part of a URL. We'll get to the other parts of a URL later.

For example, the URL `https://example.com/path` has a hostname of `example.com`. The `https://` and `/path` portions aren't part of the `domain name -> IP address` mapping that we've been learning about.

## Using the URL API in Python

The `URL` API is built into Python urllib module. You can create a [new URL object](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse):

```python
from urllib.parse import urlparse
url_parsed = urlparse('https://example.com/example-path')
```

And then you can [extract just the hostname](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse):

```python
url_parsed.netloc
```

## Assignment

Complete the `get_domain_name_from_url` function. Given a full URL, it should return the domain (or host) name.

## Expected

```
The domain name for https://boot.dev/learn/learn-python is boot.dev
```
