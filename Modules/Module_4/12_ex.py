a = int(input())
b = int(input())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12 and b == 31:
    a += 1
    b = 1
elif a == 4 or a == 6 or a == 9 or a == 11 and b == 30:
    a += 1
    b = 1
elif a == 2 and b == 28:
    a += 1
    b = 1
if a == 13:
    a = 1