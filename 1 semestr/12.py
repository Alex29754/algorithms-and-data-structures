import heapq
import os


def split_file(input_file, chunk_size):
    """Разделяет большой файл на более мелкие отсортированные подфайлы."""
    chunks = []
    with open(input_file, 'r') as f:
        lines = f.readlines(chunk_size)
        count = 0
        while lines:
            lines = list(map(int, lines))  # Преобразуем строки в числа
            lines.sort()  # Сортируем кусок данных в памяти
            chunk_file = f'chunk_{count}.txt'
            with open(chunk_file, 'w') as chunk_f:
                chunk_f.writelines(f"{line}\n" for line in lines)  # Записываем отсортированные данные в подфайл
            chunks.append(chunk_file)
            count += 1
            lines = f.readlines(chunk_size)
    return chunks


def merge_chunks(chunks, output_file):
    """Сливает отсортированные подфайлы в один окончательный отсортированный файл."""
    with open(output_file, 'w') as output_f:
        files = [open(chunk, 'r') for chunk in chunks]
        heap = []

        # Инициализация кучи начальными элементами из каждого подфайла
        for file_index, file in enumerate(files):
            line = file.readline().strip()
            if line:
                heapq.heappush(heap, (int(line), file_index))  # Добавляем элемент и индекс файла в кучу

        # Слияние
        while heap:
            smallest, file_index = heapq.heappop(heap)
            output_f.write(f"{smallest}\n")  # Записываем наименьший элемент в итоговый файл
            next_line = files[file_index].readline().strip()  # Читаем следующую строку из файла
            if next_line:
                heapq.heappush(heap, (int(next_line), file_index))  # Добавляем следующий элемент в кучу

        # Закрываем все подфайлы
        for file in files:
            file.close()


def external_multiway_sort(input_file, output_file, chunk_size=1024):
    """Выполняет внешнюю многофазную сортировку."""
    chunks = split_file(input_file, chunk_size)  # Разделяем файл на отсортированные подфайлы
    merge_chunks(chunks, output_file)  # Сливаем подфайлы в один итоговый файл

    # Удаление временных файлов
    for chunk in chunks:
        os.remove(chunk)


# Использование
input_file = 'large_input_file.txt'
output_file = 'sorted_output_file.txt'
chunk_size = 1024  # Размер куска, который можно загрузить в память

external_multiway_sort(input_file, output_file, chunk_size)