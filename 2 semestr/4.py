def compute_prefix_function(pattern):
    m = len(pattern)  # Длина шаблона
    pi = [0] * m  # Инициализация массива префиксной функции нулями
    k = 0  # Переменная для хранения текущей длины совпадающего префикса

    for q in range(1, m):  # Проходим по всем символам шаблона, начиная со второго
        while k > 0 and pattern[k] != pattern[q]:  # Пока k > 0 и символы не совпадают
            k = pi[k - 1]  # Возвращаемся к предыдущему значению префиксной функции
        if pattern[k] == pattern[q]:  # Если символы совпали
            k += 1  # Увеличиваем длину совпадающего префикса
        pi[q] = k  # Записываем значение префиксной функции для текущего символа

    return pi  # Возвращаем массив префиксной функции
def kmp_matcher(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    result = []

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:  # Если весь шаблон совпал
            result.append(i - m + 1)  # Записываем индекс начала вхождения
            q = pi[q - 1]  # Сдвигаем шаблон для поиска следующего вхождения
    return result
# Пример использования
text = "ababcababacaccc"
pattern = "ababac"
print(kmp_matcher(text, pattern))