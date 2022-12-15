print('месяц:')
a = int(input())
print('число:')
b = int(input())
print('год:')
c = int(input())
d = 0
if a > 12 or ((a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12) and b > 31) or ((a == 4 or a == 6 or a == 9 or a == 11) and b > 30) or (a == 2 and b > 28):
    d = 1
elif (a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12) and b == 31:
    a += 1
    b = 1
elif (a == 4 or a == 6 or a == 9 or a == 11) and b == 30:
    a += 1
    b = 1
elif a == 2 and b == 28:
    a += 1
    b = 1
else:
    b += 1
if a == 13:
    a = 1
    c += 1
if d == 0:
    print(a, b, c)
else:
    print('Введена несуществующая дата, попробуйте заново')