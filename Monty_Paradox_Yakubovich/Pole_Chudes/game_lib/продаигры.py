import random

def continue_game(words):
    choice = input('Хотите сыграть еще? да/нет ')
    if choice == 'да':
        return True
    if choice == 'нет':
        return False
    continue_game(words)

def find_word(words):
    print(words)
    word = random.choice(words)
    words.remove(word)
    return word