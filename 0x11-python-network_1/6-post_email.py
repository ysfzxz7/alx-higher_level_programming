#!/usr/bin/python3
"""
This how to make a reqs post req
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    res = requests.post(url, data={'email': email})
    print(res.text)
