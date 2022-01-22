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


def show_lines(start: int, end: int = -1):
    """
    Читает указанные строки переставляя курсор, без лишних считываний
    :param start:int
    :param end:int
    :return:
    """
    with open('bakery.csv', 'r', encoding='utf-8') as fw:
        index_row = 0
        while True:
            # Работаем только файловым курсором, по номерам строчек
            index_row += 1

            if index_row > end != -1:
                # Если вышли за рамки
                break

            if index_row >= start and (index_row <= end or end == -1):
                # Читаем только в нужном нам промежутке, без лишних считываний (!)
                row = fw.readline()
                # Если не можем читать, выходим
                if not row:
                    break
                # Если данные есть - выводим
                print(row.rstrip())
            else:
                try:
                    # Переставляем курсор
                    next(fw)
                except StopIteration:
                    break


def main(argv):
    arguments = len(argv) - 1
    if arguments > 2:
        raise AttributeError("Неверные аргументы. Пример использования: python "
                             "show_sales.py [int:вывод_с_номера] [int:вывод_по_номер]")

    if arguments == 0:
        show_lines(0, -1)

    elif arguments == 1:
        show_lines(number_attention(argv[1]))

    elif arguments == 2:
        # Можно добавить фильтрацию/валидацию и для второго аргумента, конечно же
        show_lines(number_attention(argv[1]), number_attention(argv[2]))


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
