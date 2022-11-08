import random
p=3
goals=0

while True:
    if p == 0:
        print('Ваши жизни иссякли')
        print('Количесвто правильных ответов:', goals)
        break
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    print(a, '+', b)

    answer = input()
    if (answer.isdigit()):
        answer = int(answer)
        if (a+b) == answer:
            print('Правильный ответ')
            goals += 1
        else:
            print('Neправильный ответ')
            p -= 1