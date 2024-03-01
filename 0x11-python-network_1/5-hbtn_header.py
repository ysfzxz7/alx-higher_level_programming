#!/usr/bin/python3
"""
this script is to find the X-req-id
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    id = res.headers.get('X-Request-Id')
    print(id)
