#!/usr/bin/python3
# Sends a POST request to a given URL with a given email.


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    vals = {"email": sys.argv[2]}
    donne = urllib.parse.urlencode(vals).encode("ascii")

    req = urllib.request.Request(sys.argv[1], donne)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
