#!/usr/bin/python3

import requests

REQUESTURL = "http://localhost:2224/fast"

while True:
    req = requests.get(REQUESTURL)
    if req.status_code != 200:
        break

