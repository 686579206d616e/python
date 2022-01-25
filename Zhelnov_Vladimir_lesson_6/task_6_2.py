# import socket
from sys import getsizeof
from time import perf_counter

start = perf_counter()

# Открываем файл в режиме rb, даёт небольшой прирост
#with open('nginx_logs_increased.txt', 'rb') as fr: # Проверка на 1.029.241 записей
with open('nginx_logs.txt', 'rb') as fr:
    # Создаем словарь, конечно он будет наполнятся в зависимости от размера файла
    # (!) узкое место, надеюсь не настолько сильно узкое
    spammers = {}
    # Читаем только первую часть файла, где адрес, первые 38 байт
    while True:
        chunk = fr.readline(38)
        # Если не прочли, закрываем файл
        if not chunk:
            break
        # Уходим на следующую строчку
        next(fr)
        # Если мы получаем меньше данных, то и меньше их фильтруем
        # можно конечно написать валидатор IP адресов через socket
        ip = chunk.decode('utf-8').split(' ')[0]
        if ip:
            try:
                spammers[ip] += 1
            except KeyError:
                spammers[ip] = 1

# Получаем результаты скорости парсинга
print(f'perf_counter(parse): {perf_counter() - start}')
# Сортируем полученные результаты
start = perf_counter()
top_spammers = sorted(spammers.items(), key=lambda item: item[1], reverse=True)
print("Найден ужасный спамер: %s (Запросов: %i)" % (top_spammers[0][0], int(top_spammers[0][1])))
print(f'perf_counter(sort): {perf_counter() - start}')
# Получаем результаты по памяти
print('senders.__len__:', spammers.__len__())
print('getsizeof(spammers):', getsizeof(spammers), 'bytes')
print('getsizeof(top_spammers):', getsizeof(top_spammers), 'bytes')
# print('top_spammers', top_spammers)

"""
Обычный тест на файле nginx_logs.txt
- 51.462 записей
---
    perf_counter(parse): 0.044988200000000006
    Найден ужасный спамер: 216.46.173.126 (Запросов: 2350)
    perf_counter(sort): 0.0006009000000000014
    senders.__len__: 2660
    getsizeof(spammers): 73816 bytes
    getsizeof(top_spammers): 21336 bytes

Дополнительный тест на файле nginx_logs_increased.txt
- 1.029.241 записей
---
    perf_counter(parse): 0.9528482
    Найден ужасный спамер: 216.46.173.126 (Запросов: 47000)
    perf_counter(sort): 0.0006032000000000259
    senders.__len__: 2660
    getsizeof(spammers): 73816 bytes
    getsizeof(top_spammers): 21336 bytes

* getsizeof(spammers): 0.070396 MB
* getsizeof(top_spammers): 0.020348 MB

* Максимальный разброс perf_counter(parse) может составлять +-~0.010
хотя должно зависить от оборудования, и его нагруженности

* senders.__len__ не меняется на увеличенном списке так как это просто
дубликаты тех данных что мы уже имели, а также размер spammers, top_spammers
соответственно не сильно менялся, если бы было больше уникальных IP адресов
тогда размер был бы увеличен, заметно, возможно на пару десятков тысяч байт
"""