def comb_sort(arr):
  n = len(arr)
  gap = n

  while gap > 1:
    gap //= 2
    swapped = False

    for i in range(n - gap):
      if arr[i] > arr[i + gap]:
        arr[i], arr[i + gap] = arr[i + gap], arr[i]
        swapped = True

    if not swapped:
      break

# Пример использования
my_list = [64, 34, 25, 12, 22, 11, 90]
comb_sort(my_list)
print(my_list)