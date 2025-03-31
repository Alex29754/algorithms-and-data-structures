def leftmost_point(points):
    return min(points, key=lambda p: (p[0], p[1]))


def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def jarvis_march(points):
    if len(points) < 3:
        return []

    hull = []
    start = leftmost_point(points)
    point_on_hull = start

    while True:
        hull.append(point_on_hull)
        next_point = points[0] if points[0] != point_on_hull else points[1]

        for p in points:
            if cross_product(point_on_hull, next_point, p) < 0:
                next_point = p

        point_on_hull = next_point
        if point_on_hull == start:
            break

    return hull


n = int(input("Введите количество точек: "))
points = [tuple(map(int, input().split())) for _ in range(n)]

hull = jarvis_march(points)
if hull:
    print("Выпуклая оболочка существует. Точки:", hull)
else:
    print("Выпуклая оболочка невозможна.")
