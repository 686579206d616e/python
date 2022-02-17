# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class BaseOwnExcept(Exception):
    _default_detail: str = 'base error'

    def __init__(self, detail: str = None):
        if detail:
            self._default_detail = detail

    def __str__(self):
        return self._default_detail


def div_div():
    try:
        try:
            num1 = int(input('Введите делимое: '))
            num2 = int(input('Введите делитель: '))
            return num1 / num2
        except ValueError:
            raise BaseOwnExcept("ValueError")
        except ZeroDivisionError:
            raise BaseOwnExcept("ZeroDivision")
    except BaseOwnExcept:
        # Можно ли считать что это корректная отработка?)
        return 0


print(div_div())
