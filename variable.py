class car:
    tyre = 4 #class variable
    def __init__(self):
        self.com = "HM" #instance variable
        self.mil = 11   #instance variable


c1 = car()
c2 = car()
car.tyre = 6
print(c1.com, c1.mil, c2.tyre)