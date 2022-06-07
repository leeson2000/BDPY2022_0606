from demo47 import base_url
import random
import requests

order_url = base_url % "order"

items = ['chocolate', 'glue', 'cookie', 'bread']
for _ in range(10):
    quantity = random.randint(5, 15)
    item = random.choice(items)
    result1 = requests.post(order_url, json={"item": item, "quantity": quantity})
    print(result1.status_code, result1.json())