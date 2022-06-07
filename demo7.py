courses = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
           {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
           {'name': 'andbiz3', 'field': 'android', 'attendee': 5, 'remote': False}]
print(courses)
courses[0]['name'] = 'Poop'
print(courses)
courses2 = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
            {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
            {'name': 'andbiz3', 'field': 'android', 'attendeee': 5, 'remote': False}]

print(courses2)
print(courses[2]['attendee'])
#print(courses[3]['attendee'])