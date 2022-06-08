class MyClass:
    pass


i1 = MyClass()

print(type(MyClass))
print(type(i1).__name__)
print(i1.__class__)
print(MyClass.__bases__)
print(i1.__class__.__bases__)
print(type(i1) == i1.__class__)