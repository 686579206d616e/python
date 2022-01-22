import sys
import json


"""
Есть два файла users.csv и hobby2.csv: в первом хранятся ФИО пользователей сайта, а во втором — данные об их хобби. 
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями 
— запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — 
данные о хобби (список строковых переменных). Сохранить словарь в файл task_6_3_result.json. Проверить сохранённые 
данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. 
Если наоборот — выходим из скрипта с кодом 1.

При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
"""

def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    # Ваш код пишите здесь
    result = {}
    try:
        with open(path_users_file, 'r', encoding='utf-8') as user_file:
            with open(path_hobby_file, 'r', encoding='utf-8') as hobby_file:
                for user in user_file:
                    hobbies = hobby_file.readline().rstrip().split(',')
                    fio = user.strip().split(',')
                    result[' '.join(fio)] = hobbies
    except BaseException:
        exit(1)
    return result # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)