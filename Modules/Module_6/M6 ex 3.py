lst = [int(a) for a in input().split()]
if len(lst) % 2 == 0:
    for a in range(len(lst), 2):
        lst[a], lst[a + 1] = lst[a + 1], lst[a]
    print(lst)
else:
    x = lst[-1]
    lst.pop()
    for a in range(len(lst), 2):
        lst[a], lst[a + 1] = lst[a + 1], lst[a]
    lst.append(x)
    print(lst)