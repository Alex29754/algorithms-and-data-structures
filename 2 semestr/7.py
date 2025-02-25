def max_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
        current_sum = max(current_sum, 0)

    return max_sum
arr = list(map(int, input("Введите массив чисел через пробел: ").split()))
print("Максимальная сумма подмассива:", max_subarray(arr))