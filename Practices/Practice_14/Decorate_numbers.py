import time

#Произведено исправление
def time_of_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start
        print(f"Функция {func.__name__} выполняется за {end} секунд")
    return wrapper


@time_of_function
def even_numbers_append(n):
    even_list = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


@time_of_function
def even_numbers_compresion(n):
    even_list = [i for i in range(n + 1) if i % 2 == 0]
    return even_list


even_numbers_append(10000)
even_numbers_compresion(10000)