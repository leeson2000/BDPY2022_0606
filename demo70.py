class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.day * self.member

    @classmethod
    def get_member(cls):
        return cls.member

    @staticmethod
    def calculate(x, y):
        return 2 * x ** y


t1 = Team()
# t1.day = 5
print(t1.all_working_hour())
print(t1.working_hour())

print(t1.get_member(), Team.get_member())
print(Team.calculate(2, 3), Team.calculate(3, 2))