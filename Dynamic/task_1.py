def count_paths(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        paths = [0] * (n + 1)
        paths[1] = 1
        paths[2] = 2
        paths[3] = 4

        for i in range(4, n + 1):
            paths[i] = paths[i - 1] + paths[i - 2] + paths[i - 3]

        return paths[n]


N = int(input("Введите число ступенек (N): "))

num_paths = count_paths(N)

print("Число всевозможных маршрутов мячика:", num_paths)
