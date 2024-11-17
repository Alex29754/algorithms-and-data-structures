def quick_sort(arr):
    # Базовый случай: если длина массива меньше 2, он уже отсортирован
    if len(arr) < 2:
        return arr

    # Опорный элемент (можно выбрать любой, здесь — первый)
    pivot = arr[0]

    # Элементы меньше опорного
    less = [i for i in arr[1:] if i <= pivot]

    # Элементы больше опорного
    greater = [i for i in arr[1:] if i > pivot]

    # Рекурсивный вызов для обеих частей
    return quick_sort(less) + [pivot] + quick_sort(greater)


# Пример использования:
arr = [33, 10, 68, 19, 42, 24, 77]
sorted_arr = quick_sort(arr)
print(sorted_arr)