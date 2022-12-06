#!/usr/bin/python3

import requests
import os

# define the URL we want to use
VALIDURL = "http://validate.jsontest.com/"
IPURL = "http://ip.jsontest.com/"
TIMEURL = "http://time.jsontest.com/"

def main():
    
    # use requests library to send an HTTP GET
    resp = requests.get(IPURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjsonip = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjsonip)
    myip = respjsonip["ip"]

    resp = requests.get(TIMEURL)
    respjsontime = resp.json()

    print (respjsontime.get('date'))
    mytime = respjsontime["date"]

    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    jsonTest = {}
    jsonTest["time"] = mytime
    jsonTest["ip"] = myip
    jsonTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonTest)
    print(mydata)

    # use requests library to send an HTTP POST
    resp = requests.post(VALIDURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")


if __name__ == "__main__":
    main()
