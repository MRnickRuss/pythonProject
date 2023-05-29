import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
py = urllib.request.urlopen("https://quke.ru/shop/smartfony/apple?page-size=72").read().decode()

price_pattern = r'(?:<span class="b-card2-v2__price-val">)([^<]+)'
price = re.findall(price_pattern, py)
print(price)

phone_pattern = r'(?:<a class="b-card2-v2__name" href=")(?:[^\"]+)(?:" title=")([^\"]+)'
phone = re.findall(phone_pattern, py)
print(phone)

count = 0
for i in phone:
    count += 1
print(count)

price_list = list(map(lambda x, y: (x, int(y.replace(' ', ''))), phone, price))
print(price)

j = 0
l = 0
sums = 0
max = 0
min = 111111111111111
for i in price_list:
    if i[1] > max:
        max = i[1]
        j = i
    if i[1] < min:
        min = i[1]
        l = i
    sums += i[1]
print(f'Минимал: {l}')
print(f'Максимум: {j}')
avg = sums/count
print(f'Средняя цена: {round(avg)}')

catal = open("catalog.txt", 'w')
for i in price_list:
    catal.write(' | '.join(str(s) for s in i) + '\n')
catal.write(f'\nMinimal: {str(l)} \n')
catal.write(f'Maximum: {str(j)} \n')
catal.write(f'AVG: {str(round(avg))}')