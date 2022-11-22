a = int(input())
b = int(input())
k = 0
while b != 0:
    if b > a:
        k += 1
    a = b
    b = int(input())
print(k)
