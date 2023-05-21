class Car:
    def __init__(self, color="black", type="sedan", year=2002):
        self.color = color
        self.type = type
        self.year = year

    def Start(self):
        print("Автомобиль заведен")

    def TurnOff(self):
        print("Автомобиль заглушен")

    def setColor(self, color):
        self.color = color

    def setType(self, type):
        self.type = type

    def setYear(self, year):
        self.year = year

    def showInfo(self):
        print("Color: ", self.color)
        print("Type: ", self.type)
        print("Year: ", self.year)


car = Car("white", "cabri", 2023)
car.Start()
car.TurnOff()
car.setColor("platin")
car.showInfo()