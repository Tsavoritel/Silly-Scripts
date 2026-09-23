import random
import json

class Car:
    def __init__(self, regNum, maxSpeed):
        self.regNum = regNum
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelDist = 0
    def Accelerate(self, spdChange):
        self.curSpeed += spdChange
        if self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        elif self.curSpeed < 0:
            self.curSpeed = 0
    def Drive(self):
        self.travelDist += self.curSpeed

class Race:
    def __init__(self, name, distance, cars: list):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for Car in self.cars:
            Car.Accelerate(random.randrange(-10, 15))
            Car.Drive()
        if(self.race_finished != True):
            self.race_finished()
    def print_status(self):
        everyCarsInfo = []
        for Car in self.cars:
            thisCarInfo = []
            carName = {"Name": Car.regNum}
            carTravel = {"Travel distance": Car.travelDist}
            carSpeed = {"Speed": Car.curSpeed}
            thisCarInfo.append(f"{carName}, {carTravel}, {carSpeed}")
            everyCarsInfo.append(thisCarInfo)
        print(json.dumps(everyCarsInfo, indent=2))
    def race_finished(self):
        for Car in self.cars:
            if Car.travelDist >= self.distance:
                print(f"{Car.regNum} wins !!")
                self.print_status()
                return True

cars = []
i = 0
for i in range(10):
    i += 1
    newCar = Car("ABC-" + str(i), random.randrange(100, 200))
    cars.append(newCar)

hour = 0
GDD = Race("Grand Demolition Derby", 8000, cars)
while not GDD.race_finished():
    hour += 1
    GDD.hour_passes()
    if (hour % 10 == 0):
        print(f"Hour {hour}")
        GDD.print_status()
