#!/usr/bin/python3
"""
This how to handle errors in reqs lib
"""
import sys
import requests
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        res = requests.get(url)
        print(res.text)
    except requests.exceptions.HTTPErrors as e:
        print({'Error code: {}'}.format(e.response.status_code))
