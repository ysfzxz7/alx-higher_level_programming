#!/usr/bin/python3
"""
this is the first use of requests
"""
import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
