class Elevator:
    def __init__(self, floor, topf, botf, eleNum):
        self.curFloor = floor
        self.topf = topf
        self.botf = botf
        self.eleNum = eleNum
    def floor_up(self):
        self.curFloor += 1
    def floor_down(self):
        self.curFloor -= 1
    def go_to_floor(self, floor):
        while self.curFloor < floor:
            self.floor_up()
        while self.curFloor > floor:
            self.floor_down()
        print(f"Elevator {self.eleNum} is now at floor  {self.curFloor}")

class Building:
    def __init__(self, numElevators, topf, botf = 0, elevatorList: list[Elevator] = []):
        self.numElevators = numElevators
        self.topf = topf
        self.botf = botf
        self.elevators = elevatorList

        for i in range(self.numElevators):
            newElevator = Elevator(0, topf, botf, i)
            i += 1
            elevatorList.append(newElevator)
    def run_elevator(self, elevatorNum, destFloor):
        self.elevators[elevatorNum].go_to_floor(destFloor)
    def fire_alarm(self):
        print("Fire alarm triggered !!")
        for Elevator in self.elevators:
            Elevator.go_to_floor(0)


newBuilding = Building(4, 12)
newBuilding.run_elevator(2, 11)
newBuilding.run_elevator(3, 3)
newBuilding.run_elevator(2, 5)
newBuilding.fire_alarm()