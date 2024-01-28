#!/usr/bin/python3
"""
    Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

"""
import sys
import requests
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    values = {}
    values = {"q": sys.argv[1]
              } if sys.argv[1] is not None else values["q"] == ""
    req = requests.post(url, data=values)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
