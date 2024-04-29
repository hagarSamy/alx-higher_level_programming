#!/usr/bin/python3
import urllib.request


# req = urllib.request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    page = response.read()
print("Body response:")
print("\t- type: {}".format(type(page)))
print("\t- content: {}".format(page))
print("\t- utf8 content: {}".format(page.decode('utf-8')))
