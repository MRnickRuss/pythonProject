import random


def birthday(coincidences, people):
    b_days = []
    count_true = 0
    for k in range(coincidences):
        for i in range(people):
            d = str(f'{random.randint(1, 28)} {random.randint(1, 12)}')
            if b_days.__contains__(d):
                count_true += 1
                break
            b_days.append(d)
        b_days.clear()
    a = count_true / coincidences * 100
    count_pairs = people * (people - 1) / 2
    b = count_pairs / (28 * 12) * 100
    return a % b