#!/usr/bin/python3
"""
this script to handle errors
"""
import sys
import urllib.request
import urllib.error

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as res:
        print(res.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))

