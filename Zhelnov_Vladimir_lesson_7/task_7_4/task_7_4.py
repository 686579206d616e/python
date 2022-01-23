"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
{
  100: 15,
  1000: 3,
  10000: 7,
  100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os

# fsutil file createnew <file> <size in bytes>

result = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}
walking_folder = os.path.join(os.getcwd(), 'test_folder')
for root, dirs, files in os.walk(walking_folder):
    for file in files:
        filepath = os.path.join(root, file)
        size = os.stat(filepath).st_size
        print(os.path.basename(filepath))
        if size <= 100:
            result[100] += 1
        elif 100 <= size <= 1000:
            result[1000] += 1
        elif 1000 <= size <= 10000:
            result[10000] += 1
        elif 10000 <= size <= 100000:
            result[100000] += 1

print(result)

"""
1byte
100bytes

1000bytes
111byte
200bytes

1111byte
2000bytes
2500bytes
5500bytes

15500bytes
25500bytes
75500bytes

{100: 2, 1000: 3, 10000: 4, 100000: 3}

"""