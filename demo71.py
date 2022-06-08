class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


r1 = Rectangle(2, 3)
print(r1.calculate_area())
r2 = Rectangle(4, 5)
print(r2.calculate_area())