def count_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]

    return dp[amount]


# Пример использования
coins = [1, 2, 5, 50, 100, 500, 1000, 5000]
amount = 10
print(count_ways(coins, amount))
