#!/usr/bin/python3
"""

    Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    web = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(web)
    coit = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                coit[i].get("sha"),
                coit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
