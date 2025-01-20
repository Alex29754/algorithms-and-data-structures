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

# Прямой обход (Pre-order)
def preorder(tree):
    if tree:
        print(tree[0], end=" ")  # Посетить текущий узел
        preorder(tree[1])        # Левое поддерево
        preorder(tree[2])        # Правое поддерево

# Центральный обход (In-order)
def inorder(tree):
    if tree:
        inorder(tree[1])         # Левое поддерево
        print(tree[0], end=" ")  # Посетить текущий узел
        inorder(tree[2])         # Правое поддерево

# Концевой обход (Post-order)
def postorder(tree):
    if tree:
        postorder(tree[1])       # Левое поддерево
        postorder(tree[2])       # Правое поддерево
        print(tree[0], end=" ")  # Посетить текущий узел
tree_str = "8(3(1,6(4,7)),10(,14(13,)))"
tree = parse_tree(tree_str)

print("Прямой обход :")
preorder(tree)
print("\nЦентральный обход :")
inorder(tree)
print("\nКонцевой обход :")
postorder(tree)