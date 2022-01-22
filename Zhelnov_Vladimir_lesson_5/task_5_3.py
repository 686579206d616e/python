"""
    Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Плохой Станислав']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    return ((val, klasses[key] if len(klasses) > key else None) for key, val in enumerate(tutors))


generator = check_gen(tutors, klasses)

# добавьте здесь доказательство, что создали именно генератор
print(type(generator))

# вспомогательная информация
print('tutors.length = ', len(tutors))
print('klasses.length = ', len(klasses))

for _ in range(len(tutors)):
    print(_, next(generator))

# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

'''
    Результат:
        <class 'generator'>
        tutors.length =  9
        klasses.length =  8
        0 ('Иван', '9А')
        1 ('Анастасия', '7В')
        2 ('Петр', '9Б')
        3 ('Сергей', '9В')
        4 ('Дмитрий', '8Б')
        5 ('Борис', '10А')
        6 ('Елена', '10Б')
        7 ('Станислав', '9А')
        8 ('Плохой Станислав', None)
'''
