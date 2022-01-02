def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    # list_out = ['Привет, %s!' % (x.split(' ')[-1].capitalize()) for x in list_in]
    # Не создавать новый список:
    for idx, x in enumerate(list_in):
        list_in[idx] = 'Привет, %s!' % (x.split(' ')[-1].capitalize())
    # print(id(list_in))
    return list_in


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# print(id(my_list))
result = convert_name_extract(my_list)
print(result)
