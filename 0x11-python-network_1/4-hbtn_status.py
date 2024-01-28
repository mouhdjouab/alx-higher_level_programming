#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status."""
import requests
if __name__ == "__main__":
    respone = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(respone.text)))
    print("\t- content: {}".format(respone.text))
