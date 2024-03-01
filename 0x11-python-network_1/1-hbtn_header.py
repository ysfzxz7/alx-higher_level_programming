#!/usr/bin/python3
"""
    this script to the X-REQUEST-ID
"""
import sys
import urllib.request

with urllib.request.open(sys.arg[1]) as response:
    x-request = response.getheader('X-Request-Id')
print(x-request)
