import json

bdpy = {'name': "BDPY", 'instructor': "Mark Ho", "duration": 35,
        'location': ['taipei', 'remote']}
print(bdpy)
print(type(bdpy))

courseString = json.dumps(bdpy)
print(courseString)
print(type(courseString))

obj1 = json.loads(courseString)
print(type(obj1))
for k, v in obj1.items():
    print(f"key={k}, value={v}")
