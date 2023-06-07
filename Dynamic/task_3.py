def minimum_cost(steps, costs):
    dp = [float('inf')] * (steps + 1)
    dp[0] = 0
    dp[1] = costs[0]

    for i in range(2, steps + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + costs[i - 1]

    return dp[steps]


n = int(input())
costs = list(map(int, input().split()))

result = minimum_cost(n, costs)
print(result)
