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
    def Drive(self, hours):
        self.travelDist += self.curSpeed * hours

cars = []

i = 0
for i in range(10):
    i += 1
    newCar = Car("ABC-" + str(i), random.randrange(100, 200))
    cars.append(newCar)

finishedRace = False
while finishedRace == False:
    for Car in cars:
        Car.Accelerate(random.randrange(-10, 15))
        Car.Drive(1)
        if Car.travelDist >= 10000:
            finishedRace = True
            print(f"{Car.regNum} wins !!")

everyCarsInfo = []
for Car in cars:
    thisCarInfo = []
    carName = {"Name": Car.regNum}
    carTravel = {"Travel distance": Car.travelDist}
    carSpeed = {"Speed": Car.curSpeed}
    thisCarInfo.append(f"{carName}, {carTravel}, {carSpeed}")
    everyCarsInfo.append(thisCarInfo)
print(json.dumps(everyCarsInfo, indent=2))
