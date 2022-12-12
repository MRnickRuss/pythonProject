lst = [int(a) for a in input().split()]
tsl = [int(b) for b in input().split()]
c=0
for a in range(len(lst)):
    for b in range(len(tsl)):
        if lst[a] == tsl[b]:
            c+=1
            break
print(c)