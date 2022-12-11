slovar = {}
for word in input().split():
    slovar[word] = slovar.get(word, 0)
    print(slovar[word], end='')
    slovar[word] += 1