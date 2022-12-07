#!/usr/bin/python3

import requests
import time

REQUESTURL = "http://localhost:2224/fast"

while True:
    req = requests.get(REQUESTURL)
    time.sleep(10)
    if req.status_code != 200:
        break

