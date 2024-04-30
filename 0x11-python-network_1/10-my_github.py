#!/usr/bin/python3
'''
a Python script that takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id
using --Basic Authentication--
'''


if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/user'
    usrnm = sys.argv[1]
    psswd = sys.argv[2]
    response = requests.get(url, auth=(usrnm, psswd))
    response = response.json()
    try:
        print(response['id'])
    except KeyError:
        print("None")
