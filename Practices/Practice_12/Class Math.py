class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b if not self.b == 0 else print("На ноль делить нельзя")

    def subtraction(self):
        return self.a - self.b


num = Math(2, 4)
print(num.addition())
print(num.multiplication())
print(num.division())
print(num.subtraction())
print(" --------------- ")

zero_num = Math(0, 2)
print(zero_num.division())
print(" --------------- ")

bad_num = Math(2, 0)
print(bad_num.division())
print(" --------------- ")