#!/usr/bin/python3
"""Sends a POST request to URL with  email.

"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    vals = {"email": sys.argv[2]}
    donnes = urllib.parse.urlencode(vals).encode("ascii")

    req = urllib.request.Request(url, donnes)
    with urllib.request.urlopen(req) as response:
        bod = response.read().decode("utf-8")
        print(bod)
