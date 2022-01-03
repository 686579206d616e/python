from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    str_out = ""
    for x in list_in:
        integral, fraction = divmod(x, 1.0)
        str_out += "%2.0f руб %02.0f коп, " % (integral, fraction * 100)
    return str_out.rstrip(', ')


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
init_id = id(my_list)
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
if id(result_2) == init_id:
    print('Объект списка после сортировки остался тот же')
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
# if id(result_3) != init_id:
#     print('Объект списка изменился')
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_out = sorted(list_in, reverse=True)[:5]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
