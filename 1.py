def check_brackets_type(expression):
    stack = []
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return len(stack) == 0


def main():
    print("Введите строку:")
    expression = input().strip()

    if not expression:
        print("Строка не существует")
    elif check_brackets_type(expression):
        print("Строка существует")
    else:
        print("Строка не существует")


if __name__ == "__main__":
    main()
