lst = [int(a) for a in input().split()]
for a in range(1, len(lst)):
    if lst[a] > lst[a-1]:
        print(lst[a])
