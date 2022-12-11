lst = [int(a) for a in input().split()]
lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
print(lst)