slovar = {}
n = int(input())
for i in range(n):
    a = input().split()
    slovar[a[0]] = a[1]
    slovar[a[1]] = a[0]
print(slovar[input()])
