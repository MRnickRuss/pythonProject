import re

f = open('title.txt', 'r', encoding='utf-8')
text = f.readlines()
data = []
for a in text:
    info = re.match(r'(^Рейс\s\d{3}\s(?:прибыл|отправился)\s(?:из|в)\s\w{4,10}\sв\s\d{2}:\d{2}:\d{2})', a)
    if info is not None:
        data.append(info[0])
list = []
for a in data:
    time = re.search(r'\d{2}:\d{2}:\d{2}', a).group(0)
    train_number = re.search(r'\d{3}', a).group(0)
    city = re.search(r'(?:из|в)\s\w{4,10}', a).group(0)
    list.append(f'[{time}] - Поезд № {train_number} {city}')
f = open('list', 'a', encoding='utf-8')
if len(text) != 0:
    f.seek(0)
f.write('\n'.join(list))
