a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a % 2 == 1:
    if b % 2 == 1:
        First = "Чёрная"
    else:
        First = "Белая"
else:
    if b % 2 == 1:
        First = "Белая"
    else:
        First = "Чёрная"
if c % 2 == 1:
    if d % 2 == 1:
        Second = "Чёрная"
    else:
        Second = "Белая"
else:
    if d % 2 == 1:
        Second = "Белая"
    else:
        Second = "Чёрная"
if First == Second:
    print("Да")
else:
    print("Нет")