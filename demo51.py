from demo48 import order_url
import requests

res = requests.get(order_url)
all_records = res.json()
records = {}
for k in all_records:
    # print(k)
    order = all_records[k]
    records.setdefault(order['item'], 0)
    records[order['item']] += order['quantity']
print(records)