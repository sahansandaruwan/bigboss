#https://randomuser.me/api/

import requests
import json
url = 'https://randomuser.me/api/'

rl = requests.get(url).json()
Rurl = json.dumps(rl)
x = json.loads(Rurl)
print(x)
name = x['results'][0]["gender"]
print(name)