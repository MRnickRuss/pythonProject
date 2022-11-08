import random


def game(iterations):
    agree = 0
    not_agree = 0
    for i in range(iterations):
        a = [0, 1, 0]

        choice = random.randint(0, 2)
        a.pop(choice)
        a.remove(0)

        if a[0] == 1:
           agree += 1
        else:
           not_agree += 1

    return f'agree: {agree/iterations * 100}\nnot agree: {not_agree/iterations * 100}'
