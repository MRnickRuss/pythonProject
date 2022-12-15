n = int(input())
position = 0
fibi = 1
b = 0
c = 0
while True:
    position += 1
    c = fibi
    fibi += b
    b = c
    if (b >= n):
        if (b == n):
            print(position)
        else:
            print(-1)
        break