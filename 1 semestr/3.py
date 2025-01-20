def find_numbers(x):
    numbers = set()

    # Перебираем значения для K, L, M
    for K in range(0, int(x ** 0.5) + 1):  # Значение K, чтобы 3^K не превысило x
        for L in range(0, int(x ** 0.5) + 1):  # Значение L, чтобы 5^L не превысило x
            for M in range(0, int(x ** 0.5) + 1):  # Значение M, чтобы 7^M не превысило x
                num = (3 ** K) * (5 ** L) * (7 ** M)
                if num <= x:
                    numbers.add(num)

    # Преобразуем множество в отсортированный список и выводим
    sorted_numbers = sorted(numbers)
    return sorted_numbers


# Пример использования
x = int(input("Введите число x: "))
result = find_numbers(x)
print("Числа, удовлетворяющие условию:")
print(result)


# def find_numbers(x):
#     numbers = set()
#
#     K = 0
#     while 3 ** K <= x:  # Перебираем K, пока 3^K не превышает x
#         L = 0
#         while (3 ** K) * (5 ** L) <= x:  # Перебираем L, пока 3^K * 5^L не превышает x
#             M = 0
#             while (3 ** K) * (5 ** L) * (7 ** M) <= x:  # Перебираем M, пока 3^K * 5^L * 7^M <= x
#                 numbers.add((3 ** K) * (5 ** L) * (7 ** M))
#                 M += 1
#             L += 1
#         K += 1
#
#     # Преобразуем множество в отсортированный список и выводим
#     sorted_numbers = sorted(numbers)
#     return sorted_numbers
#
#
# # Пример использования
# x = int(input("Введите число x: "))
# result = find_numbers(x)
# print("Числа, удовлетворяющие условию:")
# print(result)
