class Team:
    name = "[Normal Team]"


t1 = Team()
print(Team.__dict__)
print(t1.__dict__)
print(Team.name, t1.name)

t1.name = "[R&D Team]"
print(Team.__dict__)
print(t1.__dict__)
print(Team.name, t1.name)

del t1.name
print(Team.__dict__)
print(t1.__dict__)
print(Team.name, t1.name)

t1.member = 7
t1.name = "[R&D Team]"
print(Team.__dict__)
print(t1.__dict__)
print(t1.name, t1.member)