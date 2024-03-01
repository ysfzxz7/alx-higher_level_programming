#!/usr/bin/python3
"""
This script is an exemple of post req by urllib
"""
import sys
import urllib.request
import urllib.parse
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    encoded_data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data=encoded_data)
    with urllib.request.urlopen(req) as res:
        html = res.read()
    print(html.decode('utf-8'))
