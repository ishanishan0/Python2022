#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def movement(self, movetype, speed):
        self.movetype = movetype
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype, cartype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
        self.cartype = cartype

    def movement(self, movetype, speed):
        super().movement(movetype, speed)
        print("Moving my ", self.enginetype, self.cartype, " car in ", self.movetype, "at ", self.speed, " mph")

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else: 
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def movement(self, movetype, speed):
        super().movement(movetype, speed)
        print("Moving my ", self.enginetype, " motorcycle in ", self.movetype, "at ", self.speed, " mph")

car1 = Car("gas", "sports")
car2 = Car("electric", "sedan")
mc1 = Motorcycle("gas", True)

# print(mc1.wheels)
# print(car1.enginetype)
# print(car2.doors)

car1.movement("forward", 110)
car2.movement("reverse", 10)
mc1.movement("forward", 235)
