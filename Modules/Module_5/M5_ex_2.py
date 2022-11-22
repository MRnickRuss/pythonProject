a = int(input())
d = 0
while 2**d<=a:
    d+=1
print(d-1, 2**(d-1))