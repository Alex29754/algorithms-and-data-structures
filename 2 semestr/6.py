def rabin_karp(text, pattern, base=256, prime=101):
    n, m = len(text), len(pattern)
    pattern_hash = 0
    window_hash = 0
    h = 1  # Вспомогательный множитель

    # Вычисляем h = (base^(m-1)) % prime
    for _ in range(m - 1):
        h = (h * base) % prime

    # Вычисляем хеш-значение образца и первого окна в тексте
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    # Поиск подстроки
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:  # Проверка на совпадение
                return i  # Найдено в позиции i

        # Обновляем хеш-значение окна
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * h) * base + ord(text[i + m])
            window_hash %= prime  # Убедимся, что хеш положительный

    return -1  # Если не найдено

# Пример использования
text = "hello world"
pattern = "world"
print(rabin_karp(text, pattern))  # Выведет 6
