#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


import requests
my_url = "https://alx-intranet.hbtn.io/status"
with requests.get(my_url) as my_response:
    if my_response.status_code == 200:
        print(
            "Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}".format(
                type(my_response.text),
                my_response.text))
# #!/usr/bin/python3
# '''
# a Python script that fetches https://alx-intranet.hbtn.io/status
# '''


# if __name__ == "__main__":
#     import requests
#     url = "https://alx-intranet.hbtn.io/status"
#     response = requests.get(url)
#     print("Body response:")
#     res = response.text
#     print("\t- type: {}".format(type(res)))
#     print("\t- content: {}".format(res))
