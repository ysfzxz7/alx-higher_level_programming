#!/usr/bin/python3
"""
    Status module, for fetching a URL.
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as respose:
        data = response.read()
        print(f"""Body response:
        - type: {type(data)}
        - content: {data}
        - utf8 content: {data.decode('utf-8')}""")
