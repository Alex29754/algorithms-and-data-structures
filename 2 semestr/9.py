def tsp(dist):
    n = len(dist)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Начинаем с города 0

    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == float('inf'):
                continue
            for j in range(n):
                if not (mask & (1 << j)):
                    dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + dist[i][j])

    # Возвращаем минимальную стоимость полного цикла
    return min(dp[(1 << n) - 1][i] + dist[i][0] for i in range(n))

# Пример использования
dist = [
    [0, 8, 4, 10],
    [8, 0, 7, 5],
    [4, 7, 0, 3],
    [10, 5, 3, 0]
]
print(tsp(dist))