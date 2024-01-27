#!/usr/bin/python3
# script that takes in a URL and an email, sends a POST request to the
# passed URL with the email as a parameter, and displays the body of the
# response (decoded in utf-8)
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode
url = f"{sys.argv[1]}"
vals = {"email ": f"{sys.argv[2]}"}
data = urlencode(vals).encode("ascii")
with urlopen(Request(url, data)) as response:
    print(response.read().decode("utf-8"))
