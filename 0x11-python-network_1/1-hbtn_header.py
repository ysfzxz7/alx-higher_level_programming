#!/usr/bin/python3
"""
    this script to the X-REQUEST-ID
"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    request = response.getheader('X-Request-Id')
print(request)
