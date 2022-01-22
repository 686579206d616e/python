"""
    Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
        src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
        result = [12, 44, 4, 10, 78, 123]
    Подсказка: использовать возможности python, изученные на уроке.
"""


def get_numbers(src: list):
    """ Используем возможности изученные на уроке: генератор """
    prev = 0
    for _ in src:
        if 0 < prev < _:
            yield _
        prev = _


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# print(get_numbers(src))
# <generator object get_numbers at 0x00000163176A96D0>

print(*get_numbers(src))
# Ожидаемый result = [12, 44, 4, 10, 78, 123]
# Действительный print = 12 44 4 10 78 123
