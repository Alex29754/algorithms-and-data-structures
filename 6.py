def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    # Меняем местами минимальный элемент и текущий элемент
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print(my_list)