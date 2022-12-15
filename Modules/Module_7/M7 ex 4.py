words = {}
n = int(input())
for i in range(n):
    a = input().split()
    for j in range(len(a)):
        if not a[j] in words:
            words[a[j]] = 0
        words[a[j]] += 1
max = 1
WxW = {}
for i in words:
    if words[i] > max:
        max = words[i]
for i in words:
    if words[i] == max:
        WxW[i] = words[i]
WxW = dict(sorted(WxW.items()))
for i in WxW:
    print(i)
    break