def tsp(graph, start):
    n = len(graph)
    visited = (1 << n) - 1
    memo = {}

    def dfs(node, visited):
        if visited == 0:
            return graph[node][start]

        if (node, visited) in memo:
            return memo[(node, visited)]

        ans = float('inf')
        for i in range(n):
            if visited & (1 << i):
                ans = min(ans, graph[node][i] + dfs(i, visited ^ (1 << i)))

        memo[(node, visited)] = ans
        return ans

    return dfs(start, visited)