def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j] , arr[j - 1] = arr[j-1], arr[j]
            else:
                break


        # Пример использования
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print(my_list)