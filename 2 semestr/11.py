def greedy_coloring(graph):
    n = len(graph)
    result = [-1] * n  # -1 = вершина не раскрашена
    result[0] = 0  # первую вершину красим в цвет 0

    for u in range(1, n):
        # Смотрим, какие цвета заняты у соседей
        used_colors = set(result[v] for v in graph[u] if result[v] != -1)

        # Назначаем первый доступный цвет
        for color in range(n):
            if color not in used_colors:
                result[u] = color
                break

    return result

# Новый граф с 5 вершинами:
# 0 — 1 — 2
# |     \ |
# 4 ——  3
graph = {
    0: [1, 4],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [0, 3]
}

# Выполняем раскраску
coloring = greedy_coloring(graph)

# Красивый вывод
print("Результат жадной раскраски:")
for vertex, color in enumerate(coloring):
    print(f"Вершина {vertex}: цвет {color}")

# Выводим общее количество использованных цветов
unique_colors = set(coloring)
print(f"\nВсего использовано цветов: {len(unique_colors)}")
