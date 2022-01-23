"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
{
  100: (15, ['txt']),
  1000: (3, ['py', 'txt']),
  10000: (7, ['html', 'css']),
  100000: (2, ['png', 'jpg'])
}
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os
import json
import sys
from pprint import pprint


# fsutil file createnew <file> <size in bytes>

def size_get(list_files: list, min_size: int, max_size: int):
    count = 0
    exts = set()
    for filechunk in list_files:
        if min_size <= filechunk[1] <= max_size:
            exts.add(filechunk[0])
            count += 1
    return count, list(exts)


folder = "test_folder"

# [('bat', 1620), ('bat', 1074), ('woff', 98164), ('csv', 7918), ('woff', 5016), ('woff', 34196),
# ('csv', 7918), ('csv', 0), ('csv', 502), ('rtf', 7), ('txt', 0)]
files = [(file.split('.')[-1], os.stat(os.path.join(root, file)).st_size)
         for root, dirs, files in os.walk(os.path.join(os.getcwd(), folder))
         for file in files if
         100000 >= os.stat(os.path.join(root, file)).st_size]
# print(sys.getsizeof(files), 'bytes')

result = {
    100: size_get(files, -1, 100),
    1000: size_get(files, 100, 1000),
    10000: size_get(files, 1000, 10000),
    100000: size_get(files, 10000, 100000)
}

pprint(result)

with open('test_folder_summary.json', 'w') as f:
    json.dump(result, f)

"""
{100: (3, ['csv', 'rtf', 'txt']),
 1000: (1, ['csv']),
 10000: (5, ['woff', 'csv', 'bat']),
 100000: (2, ['woff'])}
"""

"""
.:
total 1732
1620 Jan 23 16:46 ascii_to_unicode.bat
1074 Jan 23 16:46 bios_date.bat
4096 Jan 23 17:15 bmp
98164 Jan 23 16:43 fontawesome-webfont.woff -> 100000
4096 Jan 23 17:15 fonts
4096 Jan 23 17:15 pfb
7918 Jan 23 16:47 sample4.csv
823680 Jan 23 16:45 sample_640×426.fts
817952 Jan 23 16:46 sample_640×426.ras

./bmp:
total 976
818058 Jan 23 16:45 sample_640×426.bmp
179582 Jan 23 16:45 sample_640×426.cur

./fonts:
total 48
4096 Jan 23 17:15 csv
5016 Jan 23 16:44 NotoSansShavian-Regular.woff
34196 Jan 23 16:44 SourceCodePro-Regular.woff -> 100000

./fonts/csv:
total 8
7918 Jan 23 16:47 sample4.csv

./pfb:
total 252
249833 Jan 23 16:44  fontawesome-webfont.pfb -> wrong
502 Jan 23 17:11  sample1.csv
0 Jan 23 17:11 'sample1 — копия.csv'
7 Jan 23 17:13 'Новый документ в формате RTF.rtf'
0 Jan 23 17:13 'Новый текстовый документ.txt'
"""
