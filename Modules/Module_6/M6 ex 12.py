str = ('In the hчё-то тамh hobbit')
h = str.find('h')
hh = str.rfind('h')
print(str[:h+1], str[h+1:hh].replace('h', 'H'), str[hh:], sep='')