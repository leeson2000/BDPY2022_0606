from demo47 import url1, url2, url3
from demo48 import order_url
import requests

urls = [url1, url2, url3]

for u in urls:
    res = requests.get(u)
    print(res.status_code, res.json())
