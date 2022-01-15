"""
    Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
"""


def odd_nums(number: int) -> int:
    """ Возвращаем числа """
    for _ in range(1, number + 1, 2):
        yield _


n = 15
generator = odd_nums(n)
# Этот цикл является подсказкой?)
for _ in range(1, n + 1, 2):
    print(next(generator))

# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

'''
1
3
5
7
9
11
13
15
'''