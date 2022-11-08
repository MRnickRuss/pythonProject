import random


def get_brthp(a, b):
    summa = 0
    for i in range(b):
        list_1 = []
        for j in range(a):
            c = random.randint(1, 365)
            if c in list_1:
                summa += 1
                break
            list_1.append(c)
    return(f'Процент совпадений д.р. равен = {summa / b * 100}')