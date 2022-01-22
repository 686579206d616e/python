import io

def number_attention(num: str) -> int:
    """
    Преобразует строку в число, если не может выкидывает ValueError
    :param num:str
    :return:
    """
    try:
        return int(num)
    except ValueError:
        raise ValueError("В параметрах принимается только числа")


def change_value(index: int, value: str):
    """
    Заменяет значение на строке
    :param index:int
    :param value:str
    :return:
    """
    with open('bakery.csv', 'r+', encoding='utf-8') as fw:
        end_line = fw.seek(0, io.SEEK_END)
        offset = (index - 1) * (21 + 1)
        if offset < end_line:
            fw.seek(offset)
            fw.write("%s\n" % value.ljust(20))
        else:
            raise ValueError("Введена неверная строчка")


def main(argv):
    arguments = len(argv) - 1
    if arguments != 2:
        raise AttributeError("Неверные аргументы. Пример использования: python "
                             "change_sale.py [Порядковый_номер_числа] [Значение]")

    if len(argv[2]) <= 20:
        change_value(number_attention(argv[1]), argv[2])
    else:
        raise ValueError("Вы ввели слишком большое число")


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
