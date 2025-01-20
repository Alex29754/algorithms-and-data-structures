def maximumSubarraySum(numbers):
    max_sum = -10 ** 100  # Инициализация минимальной суммой
    best_subarray = []  # Подмассив с максимальной суммой

    for i in range(len(numbers)):
        current_sum = 0
        for j in range(i, len(numbers)):
            current_sum += numbers[j]

            # Проверяем, нужно ли обновить максимальную сумму
            if max_sum < current_sum:
                max_sum = current_sum
                best_subarray = numbers[i:j + 1]  # Сохраняем текущий подмассив

    print("Подмассив с максимальной суммой:", best_subarray)
    print("Максимальная сумма:", max_sum)


# Ввод массива
numbers = list(int(input("Введите число: ")) for i in range(int(input("Введите длину массива: "))))
maximumSubarraySum(numbers)
