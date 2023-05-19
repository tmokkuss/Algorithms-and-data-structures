import random
import time


def bubble_sort(arr):
    """Простой алгоритм пузырьковой сортировки"""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_v2(arr):
    """Добавил флаг"""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def bubble_sort_v3(arr):
    """Добавил индекс последнего обмена"""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        last_swap_index = 0
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                last_swap_index = j
        if not swapped:
            break
        n = last_swap_index + 1


def generate_random_lists(num_lists):
    lists = []
    for _ in range(num_lists):
        length = random.randint(1000, 10000)
        lst = [random.randint(0, 100000) for _ in range(length)]
        lists.append(lst)
    return lists


def compare_sorting():
    num_lists = 4
    lists = generate_random_lists(num_lists)

    for i, lst in enumerate(lists):
        print(f"Список {i+1}: Длина {len(lst)}")

        start_time = time.time()
        bubble_sort(lst.copy())
        bubble_sort_time = time.time() - start_time
        print(f"Пузырьковая сортировка: {bubble_sort_time:.6f} сек")

        start_time = time.time()
        bubble_sort_v2(lst.copy())
        bubble_sort_time = time.time() - start_time
        print(f"Пузырьковая сортировка v2: {bubble_sort_time:.6f} сек")

        start_time = time.time()
        bubble_sort_v3(lst.copy())
        bubble_sort_time = time.time() - start_time
        print(f"Пузырьковая сортировка v3: {bubble_sort_time:.6f} сек")

        start_time = time.time()
        sorted(lst.copy())
        sorted_time = time.time() - start_time
        print(f"sorted: {sorted_time:.6f} сек")

        print("-" * 50)


compare_sorting()
