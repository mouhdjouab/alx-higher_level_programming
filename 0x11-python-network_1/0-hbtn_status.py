#!/usr/bin/python3
# script to make request with urlib library

from urllib.request import Request, urlopen
with urlopen(Request("https://alx-intranet.hbtn.io/status")) as response:
    body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
