class Car:
    vendor = "Lexus"
    valid = True


c1 = Car()
c2 = Car()
c1.color = "RED"
print(dir(Car))
print(Car.__dict__)
print(dir(c1))
print(c1.__dict__)
Car.function = True
print(Car.function, c1.function)
print(Car.__dict__)
print(c1.__dict__)
print(c2.__dict__)
print(hasattr(c1, "color"), hasattr(c2, "color"))
print(hasattr(Car, "function"), hasattr(c1, "function"), hasattr(c2, "function"))
print(c1.color, Car.function, c1.function)