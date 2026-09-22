class Car:
    def __init__(self, regNum, maxSpeed):
        self.regNum = regNum
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelTime = 0
    def Accelerate(self, spdChange):
        self.curSpeed += spdChange
        if self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        elif self.curSpeed < 0:
            self.curSpeed = 0
    def Drive(self, hours):
        self.travelTime += self.curSpeed * hours


newCar = Car("ABC-123", "142")

print(f"Your new car's registration number is {newCar.regNum}," +
      "\nit's max speed is {newCar.maxSpeed} km/h," +
      "\nand it's current speed is {newCar.curSpeed}.")

newCar.Accelerate(30)
newCar.Accelerate(70)
newCar.Accelerate(50)

print(f"Now, the current speed of your new car is {newCar.curSpeed}")

newCar.Accelerate(-200)

print(f"After using the brakes, your car's current speed is now {newCar.curSpeed}")
