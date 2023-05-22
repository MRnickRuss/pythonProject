import time


def time_of_function(func):
    start = time.perf_counter()
    result = func(10000)
    end = time.perf_counter() - start
    print(f"Функция {func.__name__} выполняется за {end} секунд")
    return result


@time_of_function
def even_numbers_append(n):
    even_list = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


@time_of_function
def even_numbers_comprehension(n):
    even_list = [i for i in range(n + 1) if i % 2 == 0]
    return even_list
