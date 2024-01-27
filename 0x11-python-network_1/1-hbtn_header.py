#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL and displays the
# value of the X-Request-Id
from sys import argv
from urllib.request import Request, urlopen

if len(argv) == 2:
    req = Request(f"{argv[1]}")
    with urlopen(req) as response:
        item = response.headers
        print(item["X-Request-Id"])
else:
    print(" Please enter the URL")
