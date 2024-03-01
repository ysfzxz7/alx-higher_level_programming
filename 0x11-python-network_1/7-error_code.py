#!/usr/bin/python3
"""
Script that:
    - takes in a URL
    - sends a request to the URL and displays the body of the response.
Usage:
    ./7-error_code.py URL.
"""

import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print({'Error code: {}'}.format(res.status_code))
    else:
        print(res.text)
