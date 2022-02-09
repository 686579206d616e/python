def val_checker(validate_function):
    """ Декоратор с валидирующей функцией, ну либо другой """
    def _logger(func):
        def wrapper(*args, **kwargs):
            validate_function(args)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return _logger


def args_number_check(args):
    """ Функция проверяющая аргументы, являются ли они положительным числом """
    for number in args:
        if type(number) != int or number < 0:
            raise ValueError(f"wrong val {number}")


def args_string_check(args):
    """ Функция проверяющая аргументы, являются ли они положительным числом """
    for string in args:
        if type(string) != str or len(string) < 1:
            raise ValueError(f"wrong StringValue {string}")


""" Написать декоратор с аргументом-функцией (callback) """

# @val_checker(args_string_check)
@val_checker(args_number_check)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3
    # return x


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))

"""
125
Traceback (most recent call last):
    raise ValueError(f"wrong val {number}")
ValueError: wrong val ss
"""
