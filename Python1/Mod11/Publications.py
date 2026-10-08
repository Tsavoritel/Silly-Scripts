class Publication:
    def __init__(self, name):
        self.name = name
class Book(Publication):
    def __init__(self, author, name, page_cnt):
        super().__init__(name)
        self.author = author
        self.pageCnt = page_cnt
    def print_information(self):
        print(f"Name of magazine: {self.name} \nAuthor: {self.author} \nPages: {self.pageCnt}")
class Magazine(Publication):
    def __init__(self, chief_auth, name):
        super().__init__(name)
        self.chiefAuth = chief_auth
    def print_information(self):
        print(f"Name of magazine: {self.name} \nChief Author: {self.chiefAuth}")
        
DonaldDuck = Magazine("Donald Duck","Aki Hyyppä")
CompartmentNo6 = Book("Compartment No. 6", "Rosa", 192)
print("publication 1:")
DonaldDuck.print_information()
print("publication 2:")
CompartmentNo6.print_information()