import time


def time_of_function(func):
    start = time.perf_counter()
    result = func(2)
    end = time.perf_counter() - start
    print(f"Функция {func.__name__} выполняется за {end} секунд")
    return result


def fibonacci_cache(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        if not cache:
            for i in range(min(2, n+1)):
                cache[i] = i
        for i in range(len(cache), n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
    return wrapper


@time_of_function
def fibonacci(n):
    return n if n == 0 or n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


@time_of_function
@fibonacci_cache
def fibonacci_cached(n):
    return n if n == 0 or n == 1 else fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


print(fibonacci(10))
print(fibonacci_cached(10))
print(fibonacci_cached(20))