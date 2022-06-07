import requests
base_url = "https://leedemo-bbd58-default-rtdb.firebaseio.com/%s.json"

url1 = base_url % "lab1"

r1 = requests.put(url1, json="使用python連到firebase")
print(r1.status_code, r1.json())

bdpy = {'name': "BDPY", "instructor": "李大帥", 'announce': None, "duration": 35,
        "period": ['Mon', "Tue", "Wed", "Thr", "Fri"]}

url2 = base_url % "lab2"
r2 = requests.put(url2, json=bdpy)
print(r2.status_code, r2.json())

courses = ['andbiz', 'poop', None, None, 'bdpy']
url3 = base_url%"lab3"
r3 = requests.put(url3, json=courses)
print(r3.status_code, r3.json())