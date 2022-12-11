slovar = {}
operations = {'W': 'write', 'R': 'read', 'X': 'execute'}
for i in range(int(input())):
    a = input().split()
    slovar[a[0]] = [operations[i] for i in a[1:]]
print(slovar)
for i in range(int(input())):
    comm, b = input().split()
    print('OK' if comm in slovar[b] else 'Denied')