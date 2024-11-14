import re
# Функция для проверки правильности расстановки скобок
def check_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  # Закрывающая скобка без открывающей
            stack.pop()
    return len(stack) == 0  # Убедиться, что нет незакрытых скобок
# Функция для разбора выражения на токены (числа, операторы и скобки)
def tokenize(expression):
    return re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expression)
# Функция для выполнения операций
def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        if right == 0:
            raise ZeroDivisionError("Ошибка: Деление на ноль")
        values.append(left / right)
# Приоритет операций
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0
# Главная функция для вычисления выражения
def evaluate_expression(tokens):
    values = []  # Стек для чисел
    operators = []  # Стек для операторов
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit():  # Если токен - число, добавляем в стек чисел
            values.append(int(token))
        elif token == '(':  # Если открывающая скобка, добавляем в стек операторов
            operators.append(token)
        elif token == ')':  # Если закрывающая скобка, выполняем операции до открывающей
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Убираем '('
        elif token in "+-*/":  # Если оператор
            while operators and precedence(operators[-1]) >= precedence(token):
                apply_operator(operators, values)
            operators.append(token)
        i += 1
    # Выполнение оставшихся операций
    while operators:
        apply_operator(operators, values)
    return values[-1]
expression = input("Введите выражение: ").strip()
# Убираем знак "=" в конце
if expression.endswith('='):
    expression = expression[:-1]
# Проверка скобок
if not check_parentheses(expression):
    print("Ошибка: Скобки расставлены неправильно")
# Разбор выражения на токены
tokens = tokenize(expression)
try:
    # Вычисляем результат
    result = evaluate_expression(tokens)
    print(f"Результат: {result}")
except ZeroDivisionError as e:
    print(e)