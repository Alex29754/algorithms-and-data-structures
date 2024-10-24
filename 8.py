# # поразрядная сортировка
# def radix_sort(arr):
#     # находим размер самого длинного числа
#     max_digits = max([len(str(x)) for x in arr])
#
#     # основание системы счисления
#     base = 10
#
#     # создаём промежуточный пустой массив из 10 элементов
#     bins = [[] for _ in range(base)]
#
#     # перебираем все разряды, начиная с нулевого
#     for i in range(0, max_digits):
#         # для удобства выводим текущий номер разряда, с которым будем работать
#         print('✅ Номер разряда → ' + str(i))
#         # перебираем все элементы в массиве
#         for x in arr:
#             # получаем цифру, стоящую на текущем разряде в каждом числе массива
#             digit = (x // base ** i) % base
#             # отправляем число в промежуточный массив в ячейку, которая совпадает со значением этой цифры
#             bins[digit].append(x)
#         # собираем в исходный массив все ненулевые значения из промежуточного массива
#         arr = [x for queue in bins for x in queue]
#         # текущее состояние массива
#         print(arr)
#         # текущее состояние промежуточного массива
#         print(bins)
#
#         # очищаем промежуточный массив
#         bins = [[] for _ in range(base)]
#
#     # возвращаем отсортированный массив
#     return arr
#
#
# # запускаем сортировку
# print(radix_sort([137137105157, 24395739293, 474290561035, 5, 276, 42]))
print(len(str(474290561035)))