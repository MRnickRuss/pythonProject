class SuperStr(str):
    def __init__(self, str):
        self.str = str

    def is_repeatance(self, string):
        if not isinstance(string, str):
            return False
        repeat = len(self) / len(string)
        if repeat != round(repeat):
            return False
        if string * int(repeat) != self:
            return False
        return True

    def is_palindrom(self):
        return self == self[::-1]


s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print(s.is_repeatance("123123")) # True
print(s.is_repeatance("123123123123")) # True
print(s.is_repeatance("12312")) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
print(s) # 123123123123 (строка)
print(int(s)) # 123123123123 (целое число)
print(s + "qwe") # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom()) # True