a = input().split()
count = 1
maxCount = 1
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 1
print(maxCount)