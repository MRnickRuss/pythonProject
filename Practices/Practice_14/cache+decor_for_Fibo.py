import time
from functools import wraps

ends = 0


def time_(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global ends
        start = time.perf_counter()
        result = func(*args, **kwargs)
        ends = time.perf_counter() - start
        return result
    return wrapper


def time_of_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"Функция {func.__name__} выполняется за {end} секунд")
        return result
    return wrapper


def fibonacci_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        if not cache:
            for i in range(min(2, n + 1)):
                cache[i] = i
        for i in range(len(cache), n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]
    return wrapper


@time_
def fibonacci(n):
    return n if n == 0 or n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


@time_of_function
@fibonacci_cache
def fibonacci_cached(n):
    return n if n == 0 or n == 1 else fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


print(fibonacci(20))
print(f"Функция {ends} секунд")

print(fibonacci_cached(10000))
print(fibonacci_cached(10000))
