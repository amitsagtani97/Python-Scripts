#!/usr/bin/env python
import requests
import json
import os, platform

HOST = "http://api.giphy.com/v1/gifs/search"
PUBLIC_KEY = "dc6zaTOxFJmzC"

query = raw_input("Search giphy: ")

payload = {'q': query, 
        'rating': 'r',
        'api_key': PUBLIC_KEY, 
        'limit': 1
}

res = requests.get(HOST, params=payload)
res = res.json()

for k, v in res.items():
    if k == "data":
        data = v[0]
        for i, j in data.items():
            if i == "url":
                url = j
#url = res['data']['url']

if platform.system() == "Darwin":
    os.system("open %s" % url)
elif platform.system() == "Linux":
    os.system("xdg-open %s" % url)
else:
    print("u fukin pleb...jk")
    try:
        os.system("start %s" % url)
    except OSError as e:
        print("You done goofed: {0}".format(e))

