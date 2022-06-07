from demo47 import base_url, url2, url3
import requests

bdpy = {'name': "python與資料處理實戰演練", "course_id": "bdpy"}
r2 = requests.patch(url2, json=bdpy)
print(r2.status_code, r2.json())

patchArray = {1:"POOP!!",2:"add something",3:"試多國語言"}
r3 = requests.patch(url3, json=patchArray)
print(r3.status_code, r3.json())