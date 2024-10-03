def check_brackets_multi(string):
    round_brackets = 0  # Счётчик для круглых скобок ()
    curly_brackets = 0  # Счётчик для фигурных скобок {}
    square_brackets = 0  # Счётчик для квадратных скобок []

    for char in string:
        if char == '(':  # Открывающая круглая скобка
            round_brackets += 1
        elif char == ')':  # Закрывающая круглая скобка
            round_brackets -= 1
            if round_brackets < 0:  # Неправильное закрытие
                return "Строка не существует"

        elif char == '{':  # Открывающая фигурная скобка
            curly_brackets += 1
        elif char == '}':  # Закрывающая фигурная скобка
            curly_brackets -= 1
            if curly_brackets < 0:  # Неправильное закрытие
                return "Строка не существует"

        elif char == '[':  # Открывающая квадратная скобка
            square_brackets += 1
        elif char == ']':  # Закрывающая квадратная скобка
            square_brackets -= 1
            if square_brackets < 0:  # Неправильное закрытие
                return "Строка не существует"

    # Проверяем, что все счётчики равны нулю
    if round_brackets == 0 and curly_brackets == 0 and square_brackets == 0:
        return "Строка существует"
    else:
        return "Строка не существует"


# Пример использования
string = input("Введите строку: ")
result = check_brackets_multi(string)
print(result)
