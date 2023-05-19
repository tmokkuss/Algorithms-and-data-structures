import random
import time


def linear_search_median(arr):
    if not arr:
        return None, None
    n = len(arr)
    if n % 2 == 0:
        mid_idx = n // 2
        median = (arr[mid_idx - 1] + arr[mid_idx]) / 2
    else:
        median = arr[n // 2]
    return median


def binary_search_median(arr):
    if not arr:
        return None, None
    n = len(arr)
    mid_idx = n // 2
    if n % 2 == 0:
        median = (arr[mid_idx - 1] + arr[mid_idx]) / 2
    else:
        median = arr[mid_idx]
    return median


def generate_sorted_array(size):
    arr = [random.randint(0, 100) for _ in range(size)]
    arr.sort()
    return arr


def compare():
    sizes = [1000, 5000, 10000, 50000]
    num_trials = 10

    for size in sizes:
        print(f"Размер массива: {size}")

        linear_search_total_time = 0
        binary_search_total_time = 0

        for _ in range(num_trials):
            arr = generate_sorted_array(size)

            start_time = time.time()
            linear_search_median(arr)
            linear_search_time = time.time() - start_time
            linear_search_total_time += linear_search_time

            start_time = time.time()
            binary_search_median(arr)
            binary_search_time = time.time() - start_time
            binary_search_total_time += binary_search_time

        avg_linear_search_time = linear_search_total_time / num_trials
        avg_binary_search_time = binary_search_total_time / num_trials

        print(f"Среднее время линейного поиска: {avg_linear_search_time:.15f} сек")
        print(f"Среднее время бинарного поиска: {avg_binary_search_time:.15f} сек")
        print("-" * 50)


compare()
