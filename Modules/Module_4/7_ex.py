a = int(input())
if a % 10 == a // 1000 and a // 10 % 10 == a // 100 % 10:
    print("Да")
else:
    print("Нет")