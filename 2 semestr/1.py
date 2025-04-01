import matplotlib.pyplot as plt


def cross_product(o, a, b):
    """Вычисляет векторное произведение для трех точек o, a, b."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """Находит выпуклую оболочку множества точек с помощью алгоритма Грэхема."""
    if len(points) < 3:
        return points  # Выпуклая оболочка невозможна

    points = sorted(points)  # Сортируем точки по x, при равных x — по y

    # Строим нижнюю оболочку
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Строим верхнюю оболочку
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]  # Исключаем повторяющиеся точки


def plot_convex_hull(points, hull):
    """Визуализирует исходные точки и их выпуклую оболочку."""
    x, y = zip(*points)
    plt.scatter(x, y, label='Точки')

    hull.append(hull[0])  # Замыкаем оболочку
    hx, hy = zip(*hull)
    plt.plot(hx, hy, 'r-', label='Выпуклая оболочка')

    plt.legend()
    plt.show()


# Пример использования:
points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 3), (3, 3), (3, 1)]
hull = convex_hull(points)
print("Выпуклая оболочка:", hull)
plot_convex_hull(points, hull)