from demo48 import order_url
from demo47 import url1, url2, url3
import requests
import time

urls = [order_url, url1, url2, url3]
for url in urls:
    time.sleep(8)
    res = requests.delete(url)
    print(res.status_code)