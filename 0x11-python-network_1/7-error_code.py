#!/usr/bin/python3
"""
This how to handle errors in reqs lib
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.text)
    if res.status_code >= 400
    print({'Error code: {}'}.format(res.status_code))
