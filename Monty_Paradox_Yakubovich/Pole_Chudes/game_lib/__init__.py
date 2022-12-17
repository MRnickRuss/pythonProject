from .продаигры import *
from .гамеплей import *
from .слова_рекорд import *

words = get_words()
while True:
    word = find_word(words)
    record = play(word)
    write_record(record)
    if not continue_game(words):
        break