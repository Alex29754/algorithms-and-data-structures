def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def hash_function(item, table_size):
    return hash(item) % table_size

def create_hash_table(data, table_size):
    hash_table = [None] * table_size
    for item in data:
        index = hash_function(item, table_size)
        # Линейное пробирование
        while hash_table[index] is not None:
            index = (index + 1) % table_size
        hash_table[index] = item
    return hash_table

def write_hash_table_to_file(hash_table, output_filename):
    with open(output_filename, 'w') as file:
        for index, item in enumerate(hash_table):
            file.write(f"{index}: {item}\n")

def main(input_filename, output_filename, table_size):
    data = read_file(input_filename)
    # Преобразуем текст в набор слов или символов
    items = data.split()  # Можно разбить по пробелам или символам
    hash_table = create_hash_table(items, table_size)
    write_hash_table_to_file(hash_table, output_filename)


main("input.txt", "output.txt", 8)