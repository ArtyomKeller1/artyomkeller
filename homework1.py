import requests as r
import json
user = input()
url = f"https://api.github.com/users/{user}/repos"
data = r.get(url)
data = data.json()
with open('data.json', 'w') as f:
    json.dump(data, f)