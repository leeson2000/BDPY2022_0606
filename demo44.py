import requests
from pprint import pprint

url1 = "https://bugzilla.mozilla.org/rest/bug/35"
response = requests.get(url1)
print(response.status_code)
print(type(response.content), response.content)
print(type(response.json()), response.json())

bug35 = response.json()["bugs"][0]
print(type(bug35))
print(bug35.keys())
for cc in bug35['cc']:
    print(cc)