str = ('In the чё-то там hobbit')
h = str.find('h')
hh = str.rfind('h')
print(str[:h], str[hh:h:-1], str[hh:], sep='')