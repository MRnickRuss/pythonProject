word = input()
a = word.find("f")
b = word.rfind("f")
if a == b:
    print(a)
else:
    print(a, b)