#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

"""
import sys
import requests


if __name__ == "__main__":

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    val = {"q": letter}

    reqes = requests.post("http://0.0.0.0:5000/search_user", data=val)
    try:
        repons = reqes.json()
        if repons == {}:
            print("No result")
        else:
            print("[{}] {}".format(repons.get("id"), repons.get("name")))
    except ValueError:
        print("Not a valid JSON")
