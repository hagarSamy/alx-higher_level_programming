#!/usr/bin/python3
'''
a Python script that takes in a letter and
sends a POST request to
http://0.0.0.0:5000/search_user with the letter
as a parameter.
'''


if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    my_data = {'q': q}
    response = requests.post(url, data=my_data)
    try:
        jsonData = response.json()
        if jsonData:
            print("[{}] {}".format(jsonData['id'], jsonData['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
