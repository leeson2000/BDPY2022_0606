import collections
from pprint import pprint

# define a new namedTuple

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])


if __name__ == '__main__':
    print(type(course))
    pprint(dir(course))

    poop = course(name='poop', field='python', attendee=10, remote=False)
    print(poop)
    print(poop.name, poop.attendee)
    # poop.name='Poop'