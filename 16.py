# Определяем дерево через вложенные списки
def parse_tree(s):
    def helper(index):
        while index < len(s) and s[index] in " ,":  # Пропускаем пробелы и запятые
            index += 1

        if index >= len(s) or not s[index].isdigit():  # Если конец строки или нет числа
            return None, index

        value = 0
        while index < len(s) and s[index].isdigit():  # Считываем число
            value = value * 10 + int(s[index])
            index += 1

        node = [value, None, None]  # Узел

        if index < len(s) and s[index] == "(":  # Обработка поддеревьев
            index += 1
            node[1], index = helper(index)  # Левое поддерево
            node[2], index = helper(index) if s[index] == "," else (None, index)  # Правое поддерево
            index += 1  # Закрывающая скобка ')'

        return node, index

    return helper(0)[0]


def non_recursive_preorder(tree):
    if not tree:  # Проверяем, если дерево пустое
        return ""

    stack = [tree]  # Инициализируем стек с корневым узлом
    result = []  # Список для хранения результатов обхода

    while stack:
        node = stack.pop()  # Извлекаем верхний элемент стека
        result.append(str(node[0]))  # Добавляем значение узла в результат

        # Сначала добавляем правое поддерево, затем левое
        if node[2]:  # Правое поддерево
            stack.append(node[2])
        if node[1]:  # Левое поддерево
            stack.append(node[1])

    return " ".join(result)  # Возвращаем строку обхода


# Пример использования
tree_str = "8(3(1,6(4,7)),10(,14(13,777)))"
tree = parse_tree(tree_str)

# Нерекурсивный прямой обход
result = non_recursive_preorder(tree)
print("Нерекурсивный прямой обход:", result)