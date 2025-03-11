def bad_character_table(pattern):
    """Создаёт таблицу 'плохих символов'."""
    bad_char = {}
    length = len(pattern)

    for i in range(length - 1):
        bad_char[pattern[i]] = length - 1 - i

    return bad_char


def boyer_moore_search(text, pattern):
    """Алгоритм Бойера-Мура для поиска образца в строке."""
    m, n = len(pattern), len(text)

    if m > n:
        return -1  # Образец длиннее текста

    bad_char = bad_character_table(pattern)

    shift = 0  # Сдвиг образца относительно текста

    while shift <= n - m:
        j = m - 1  # Индекс для сравнения символов

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            return shift  # Найдено совпадение

        # Вычисляем сдвиг по эвристике "плохого символа"
        bad_char_shift = bad_char.get(text[shift + j], m)
        shift += bad_char_shift  # Двигаем образец вправо

    return -1  # Образец не найден


# 🔹 Тестирование
text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"

index = boyer_moore_search(text, pattern)
print(f"Образец найден на позиции: {index}" if index != -1 else "Образец не найден")
