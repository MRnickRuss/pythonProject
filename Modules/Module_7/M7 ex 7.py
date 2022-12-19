count = {}
a = int(input())
for i in range(a):
    a = input().split()
    for i in range(len(a)):
        if not a[i] in count:
            count[a[i]] = 0
        count[a[i]] += 1
result = []
for key, value in count.items():
    result.append(f'{value} {key}')
result.sort()
result.reverse()
for i in range(len(result)):
    a = result[i].split()
    print(a[1], a[0], sep=' ')