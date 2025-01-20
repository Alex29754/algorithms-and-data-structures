def heapify(arr, n, i):
    # Инициализация наибольшего элемента как корня
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Если левый больше корня
    if left < n and arr[i] < arr[left]:
        largest = left

    # Если правый больше, чем самый большой на данный момент
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Замена
        # Рекурсивно heapify поддерево
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Замена
        heapify(arr, i, 0)

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив:", arr)