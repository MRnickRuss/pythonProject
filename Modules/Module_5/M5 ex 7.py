position = int(input())
fibi = 1
b = 1
c = 0
d = 0
while b != position:
    b += 1
    d = fibi
    fibi += c
    c = d
print(fibi)