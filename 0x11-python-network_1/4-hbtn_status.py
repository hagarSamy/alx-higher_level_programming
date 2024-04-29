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
#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    my_url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(my_url)
    print("Body response:")
    content = req.text
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
