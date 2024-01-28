#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status."""
import requests
if __name__ == "__main__":
    respone=requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print(f"\t- type: {type(respone.text)}")
    print(f"\t- content: {respone.text}")
