"""
    *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

n = 15
generator = (_ for _ in range(1, n + 1, 2))
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