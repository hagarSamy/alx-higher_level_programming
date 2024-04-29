#!/usr/bin/python3
'''
a Python script that fetches https://alx-intranet.hbtn.io/status
'''


if __name__ == "__main__":
    import requests
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    response = response.text
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
