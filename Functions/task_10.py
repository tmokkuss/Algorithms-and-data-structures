import timeit


def tribonacci_recursive(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci_recursive(n-1) + tribonacci_recursive(n-2) + tribonacci_recursive(n-3)


def tribonacci_iterative(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__} для n = {n}: {execution_time:.6f} секунд")
        return result
    return wrapper


@measure_time
def run_tribonacci(func, n):
    return func(n)


n = 10

run_tribonacci(tribonacci_recursive, n)
run_tribonacci(tribonacci_iterative, n)
