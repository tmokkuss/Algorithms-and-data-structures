import random
import time

def nod(a, b):
    while b:
        a, b = b, a % b
    return a


def enumeration(a, b):
    max_val = max(a, b)
    while True:
        if max_val % a == 0 and max_val % b == 0:
            return max_val
        max_val += 1


def euclid(a, b):
    return abs(a * b) // nod(a, b)


def nok(a, b):
    return abs(a * b) // nod(a, b)


def generate_random_lists(num_lists):
    lists = []
    for _ in range(num_lists):
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        lists.append((num1, num2))
    return lists


def compare():
    num_lists = 4
    lists = generate_random_lists(num_lists)

    for i, (num1, num2) in enumerate(lists):
        print(f"Первое число {num1} и второе число {num2}")

        start_time = time.time()
        enum = enumeration(num1, num2)
        enum_time = time.time() - start_time
        print("Наименьшее общее кратное по алгоритму перебора:", enum)
        print(f"Алгоритм перебора: {enum_time:.6f} сек")

        start_time = time.time()
        euclidean = euclid(num1, num2)
        euclidean_time = time.time() - start_time
        print("Наименьшее общее кратное по алгоритму Евклида:", euclidean)
        print(f"Алгоритм Евклида: {euclidean_time:.6f} сек")

        start_time = time.time()
        nokian = nok(num1, num2)
        nokian_time = time.time() - start_time
        print("Наименьшее общее кратное по формуле НОК через НОД:", nokian)
        print(f"По формуле НОК через НОД: {nokian_time:.6f} сек")

        print("-" * 50)


"""Алгоритм Евклида и по формуле НОК через НОД -- лучшие"""

compare()
