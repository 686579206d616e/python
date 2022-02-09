from functools import wraps


def type_logger(func):
    """Декоратор наших экспериментов"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            manys = [f"{arg}: {type(arg)}" for arg in args]
            print(f"{func.__name__}({', '.join(manys)})")
        return func(*args, **kwargs)
    return wrapper


@type_logger
def calc_cube(x, y, z):
    """Шпионская документация"""
    return x ** 3 + y + z


print(calc_cube(3, 0, False))

print(calc_cube.__name__)
help(calc_cube)
print(calc_cube.__doc__)

"""
calc_cube(3: <class 'int'>, 0: <class 'int'>, False: <class 'bool'>)
27
calc_cube
Help on function calc_cube in module __main__:

calc_cube(x, y, z)
    Шпионская документация

Шпионская документация
"""
