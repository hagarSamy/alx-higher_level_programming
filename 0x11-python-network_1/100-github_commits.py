#!/usr/bin/python3
'''
a Python script that list 10 commits
(from the most recent to oldest)
of the repository “rails” by the user “rails”
using -- GitHub API's endpoint for listing commits--
'''


if __name__ == "__main__":
    import requests
    import sys
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)
    commits = response.json()
    for commit in commits:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
