a = int(input())
b = int(input())
if a % 2 == 1:
    if b % 2 == 1:
        print("Чёрная")
    else:
        print("Белая")
else:
    if b % 2 == 1:
        print("Белая")
    else:
        print("Чёрная")