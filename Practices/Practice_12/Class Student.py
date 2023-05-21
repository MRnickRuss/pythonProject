class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    # Возврат значения имени
    def GetName(self):
        return self.name

    # Возврат значения имени
    def GetAge(self):
        return self.age

    # Возврат значения номера
    def GetGroupNumber(self):
        return self.groupNumber

    # Изменение значений имени и возраста
    def SetNameAge(self, name, age):
        self.name = name
        self.age = age

    # Тоже, но с номером
    def SetGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def showInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("GroupNumber: ", self.groupNumber)


first = Student("Nick", 15, "10A")
first.showInfo()
print(" --------------- ")

second = Student("Oleg", 16, "9A")
second.showInfo()
print(" --------------- ")

third = Student("----", 0, "10B")
third.SetNameAge("Igor", 17)
third.showInfo()
print(" --------------- ")

forth = Student("Vlad", 18, "0A")
forth.SetGroupNumber("10A")
forth.showInfo()
print(" --------------- ")

fifth = Student()
fifth.SetNameAge("Dmitrii", 19)
forth.SetGroupNumber("10A")
fifth.showInfo()
print(" --------------- ")
