#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
"""

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header_value = response.getheader('X-Request-Id')
    print(header_value)

