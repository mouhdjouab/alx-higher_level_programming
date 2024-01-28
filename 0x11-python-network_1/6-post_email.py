#!/usr/bin/python3
"""
 Sends a POST request to a given URL with a given email.

"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    req = requests.post(url, data=values)
    print(req.text)
