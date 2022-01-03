# Задание 1, Задание 3
# Есть ли замена?
def custom_is_integer(num: str) -> bool:
    """ Определяет действительно ли строка является числом """
    try:
        int(num)
        return True
    except ValueError:
        return False


# Есть ли замена?
def two_digits(num: str) -> str:
    """ Добавляет 2х значный числовой формат """
    case = "{0:0=2d}"
    if '+' in num:
        case = "+{0:0=2d}"
    return case.format(int(num))


# Если не знать индексы, и входящие данные, то данная функция сформирует нужный формат
# join() не подходит так как невозможно сформировать пробелы между кавычками
# Данный функционал можно было написать внутри функции convert_list_in_str()
def format_str(list_in: list) -> str:
    """ Форматирует строку в указанном формате """
    result_out = ""
    offset = 0
    while True:
        if '"' not in list_in[offset]:
            result_out += list_in[offset] + " "
            offset += 1
        else:
            result_out += f"{list_in[offset]}{list_in[offset + 1]}{list_in[offset + 2]} "
            offset += 3
        if offset == len(list_in):
            break
    return result_out.strip()


# Исходя из строки в которой неизвестно какие элементы на каких местах
def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    offset = 0
    # Проверка по памяти
    # print(id(list_in))
    while True:
        if custom_is_integer(list_in[offset]) is True:
            # .insert() - дорогой с точки зрения алгоритмической сложности
            # однако, в рамках дз выполняет свою задачу
            list_in.insert(offset, '"')
            list_in[offset + 1] = two_digits(list_in[offset + 1])
            list_in.insert(offset + 2, '"')
            offset += 3
        else:
            offset += 1
        end_element = len(list_in)
        if offset == end_element:
            break
    # print(id(list_in))
    # return ' '.join(list_in)
    return format_str(list_in)


# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', 'а через', "-81",
#            'минут', "+387", 'Градус Цельсия', 'влажность', 'относительно', 'влажная']
# print(id(my_list))
result = convert_list_in_str(my_list)
print(result)
