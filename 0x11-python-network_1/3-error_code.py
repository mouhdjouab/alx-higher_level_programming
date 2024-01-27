#!/usr/bin/python3
#script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
import sys
from urllib.request import Request, urlopen
from urllib.error import  HTTPError

try:
    with urlopen(Request(sys.argv[1])) as response:
        body=response.read().decode("utf-8")
except HTTPError as e:
    print('Error code: ', e.code)
