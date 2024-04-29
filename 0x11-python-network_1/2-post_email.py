#!/usr/bin/python3
'''
a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''
if __name__ == "__main__":
    import sys
    import urllib.request
    url = sys.argv[1]
    mail = sys.argv[2]
    emailData = {'email': mail}
    encodedData = urllib.parse.urlencode(emailData).encode('utf-8')
    with urllib.request.urlopen(url, data=encodedData) as response:
        page = response.read()
        print(page)
