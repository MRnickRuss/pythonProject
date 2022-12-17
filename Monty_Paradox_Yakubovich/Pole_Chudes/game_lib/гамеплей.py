def choose_complexity():
    choice = input('\nВыберите сложность: 1 - 3 жизни, 2 - 5 жизней, 3 - 7 жизней ')
    return (2 * int(choice) + 1) if choice == '1' or choice == '2' or choice == '3' else choose_complexity()


def play(word):
    max_lives = choose_complexity()
    lives = max_lives
    print_word = []
    for i in range(len(word)):
        print_word.append('\u25A0')
    print(*print_word)
    while lives > 0:
        n = input('\nВведите букву или слово')
        if len(n) == 1:
            if n in word:
                for i in range(len(word)):
                    if word[i] == n:
                        print_word[i] = n
                print(f"Вы угадали слово!\n"
                    f"Ваше количество жизней:{lives}\n")
                print(*print_word)
                if not print_word.__contains__('\u25A0'):
                    print(f'Вы выиграли!')
                    return max_lives - lives
            else:
                lives -= 1
                print(f"Вы не угадали!\n"
                      f"Ваше количество жизней:{lives}\n")
                print(*print_word)
        elif n == word:
            print(f'Вы выиграли!')
            return max_lives - lives
        else:
            lives -= 1
            print(f"Вы не угадали!\n"
                    f"Ваше количество жизней:{lives}\n")
            print(*print_word)
    print(f"Вы проиграли!\n"
          f"Слово было {word}")
    return max_lives - lives