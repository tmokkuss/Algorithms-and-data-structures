def count_sequences(N):
    dp = [0] * (N + 1)
    dp_ones = [0] * (N + 1)

    dp[1] = 1
    dp_ones[1] = 0

    for i in range(2, N + 1):
        dp[i] = dp[i-1] + dp_ones[i-1]
        dp_ones[i] = dp[i-1]

    return dp[N] + dp_ones[N]


N = int(input("Введите длину последовательности (N): "))

num_sequences = count_sequences(N)

print("Количество искомых последовательностей:", num_sequences)
