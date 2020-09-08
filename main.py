import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]
    try:
        response = requests.get(
            "https://api.github.com/users/{}/events".format(username))
        events = json.loads(response.content)

        print(events[0]['created_at'])

    except IndexError:
        print(f"Not able to find the user name:\"{username}\"")








