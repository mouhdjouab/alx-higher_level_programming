#!/usr/bin/python3
"""Sends a request to a given URL
 displays the response body.

"""
import sys
import urllib.error
import urllib.request


url = sys.argv[1]

req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("ascii"))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
