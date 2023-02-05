# Python Fetch API

In this course, we'll be using Python built-in [urllib fetch API](https://docs.python.org/3/howto/urllib2.html) to make HTTP requests. We already used it in the last two assignments!

Ignoring concepts about async/await and loops, the `fetch` api available to us by the Python language is on urllib library, all we have to do is provide it with the parameters it requires and open the request.

## Using fetch

```python
import urllib.request

settings = {'data': None, 'headers': {'X-API-Key': API_KEY, 'Content-Type': 'application/json'},
            'origin_req_host': None, 'unverifiable': None, 'method': 'GET'}

request = urllib.request.Request(url, **settings)

with urllib.request.urlopen(request) as f:
    response = json.loads(f.read().decode('utf-8'))
```

We'll go in-depth on the various things happening in this standard `fetch` call later, but let's cover some basics for now.

* `response` is the data that comes back from the server
* `url` is the URL we are making a request to
* `settings` is an object containing some request-specific settings
* `json.loads(f.read().decode('utf-8'))` its a structure that converts the response data (pure text) from the server into a JSON (dict) object

## Assignment

Fix the bug in the code.

The problem is that we aren't waiting for the response to physically come back across the internet connection before continuing with our code.

## Expected

```sh
Healing Potion

Light Leather

Padded Leather

Haste Potion

Leather Scraps

Copper Ore

Copper Bar

Iron Ore

Iron Bar

Gold Ore
```
