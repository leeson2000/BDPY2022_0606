class Movable:
    pass


class Engine(Movable):
    pass


class Motor(Movable):
    pass


class HybridCar(Engine, Motor):
    pass


print("Movable class bases:", Movable.__bases__)
print("Engine class bases:", Engine.__bases__)
print("Motor class bases:", Motor.__bases__)
print("HybridCar class bases:", HybridCar.__bases__)