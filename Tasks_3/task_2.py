import random
import time


def linear_search(arr):
    if not arr:
        return None, None

    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val


def binary_search(arr):
    if not arr:
        return None, None

    sorted_arr = sorted(arr)
    min_val = sorted_arr[0]
    max_val = sorted_arr[-1]

    return min_val, max_val


def generate_random_lists(num_lists):
    lists = []
    for _ in range(num_lists):
        length = random.randint(1000, 10000)
        lst = [random.randint(0, 100000) for _ in range(length)]
        lists.append(lst)
    return lists


def compare_search():
    num_lists = 4
    lists = generate_random_lists(num_lists)

    for i, lst in enumerate(lists):
        print(f"Список {i+1}: Длина {len(lst)}")

        start_time = time.time()
        min_val_linear, max_val_linear = linear_search(lst.copy())
        linear_search_time = time.time() - start_time
        print(f"Линейный поиск: {linear_search_time:.6f} сек")
        print("Минимальное значение Линейного поиска:", min_val_linear)
        print("Максимальное значение Линейного поиска:", max_val_linear)

        start_time = time.time()
        min_val_binary, max_val_binary = binary_search(lst.copy())
        binary_search_time = time.time() - start_time
        print(f"Бинарный поиск: {binary_search_time:.6f} сек")
        print("Минимальное значение Бинарного поиска:", min_val_binary)
        print("Максимальное значение Бинарного поиска:", max_val_binary)

        print("-" * 50)


compare_search()

