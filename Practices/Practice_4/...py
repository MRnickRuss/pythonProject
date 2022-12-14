import re

def read_file(name):
    f = open(name, 'r', encoding='utf-8')
    text = f.read()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = text.split()
    words = list(set(words))
    words.sort()
    return words

def save_file(name, words):
    f = open(name, 'a', encoding='utf-8')
    f.write(f'Всего уникальных слов: {str(len(words))} \n\n')
    f.write('\n'.join(words))
    f.close()

words = read_file('data.txt')
save_file("count.txt", words)
