def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def hash_function(item, table_size):
    return hash(item) % table_size

def create_hash_table_with_chaining(data, table_size):
    # Инициализируем хеш-таблицу, где каждая ячейка содержит список
    hash_table = [[] for _ in range(table_size)]
    for item in data:
        index = hash_function(item, table_size)
        # Добавляем элемент в конец списка в ячейке `index`
        hash_table[index].append(item)
    return hash_table

def write_hash_table_to_file(hash_table, output_filename):
    with open(output_filename, 'w') as file:
        for index, chain in enumerate(hash_table):
            file.write(f"{index}: {chain}\n")

def main(input_filename, output_filename, table_size):
    data = read_file(input_filename)
    items = data.split()  # Разбиваем текст на слова или символы
    hash_table = create_hash_table_with_chaining(items, table_size)
    write_hash_table_to_file(hash_table, output_filename)


main("input.txt", "output.txt", 8)