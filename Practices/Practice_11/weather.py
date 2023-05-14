import json
import urllib.request
from datetime import datetime

def get_weather(city):
    resp = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f').read().decode()
    my_json = json.loads(resp)
    result = f'[{datetime.now().strftime("%H:%M:%S")}]Запрос погоды в городе: {city}\nТемпература: {my_json["main"]["temp"]}℃, {my_json["weather"][0]["description"]}\nВлажность воздуха: {my_json["main"]["humidity"]}%\nСкорость ветра: {my_json["wind"]["speed"]}м/c\nАтмосферное давление: {my_json["main"]["pressure"]}мм рт ст'
    return result

city = input('Введите название города: ')
print(get_weather(city))