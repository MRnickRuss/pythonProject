countries = {}
n = int(input())
for i in range(n):
    a = input().split()
    countries[a[0]] = list(a[1:])
numct = int(input())
result = []
for i in range(numct):
    city = input()
    b = False
    for country in countries:
        if city in countries[country]:
            result.append(country)
            b = True
            break
    if not b:
        result.append('Страна не найдена')
print(*result, sep='\n')