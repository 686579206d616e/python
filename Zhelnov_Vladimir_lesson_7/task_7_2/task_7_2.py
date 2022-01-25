"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные
о вложенных папках и файлах (добавлять детали)?
"""

# Единственное что будем использовать os
import os


def go_upper(givenpath: str, steps: int = 0) -> str:
    """ Откручиваем назад путь на указанное кол-во шагов """
    split_char = '\\' if '\\' in givenpath else '/'  # для поддержки Linux, Windows
    for _ in range(steps):
        # Может есть какая-то нормальная функция встроенная?
        givenpath = givenpath.split(split_char)[0:-1]
        givenpath = split_char.join(givenpath)
    return givenpath


def config_to_live(files: list) -> bool:
    """ Создает файлы из списка """
    for gofile in files:
        # Если файл/папка существует - не создаём, не уничтожаем, хотя могли бы
        if os.path.exists(gofile):
            continue
        else:
            name = os.path.basename(gofile)
            # Если это файл - создаем
            if '.' in name:
                with open(gofile, 'x'):
                    pass
            else:
                # Создаём папку
                os.makedirs(gofile)


def config_to_dict(lines: list) -> list:
    """ Парсит конфиг и выдаёт список файлов """
    files = []
    current_base = os.getcwd()
    previous_index = -1
    for index, row in enumerate(lines):
        strip_row = row.strip()
        # Пропускаем комментарии
        if row[0] == '#' or (row[0] == '/' and row[1] == '/'):
            continue
        if len(strip_row) < 1:
            continue
        # Считаем отступы как в питоне
        indent = row.count('    ')
        # Если это директория
        if ':' in row:
            # Получаем название директории
            folder_name = strip_row[0:-1]
            # Понимаем куда нам двигаться
            next = indent - previous_index
            # Двигаемся вперед
            if next > 0:
                folder = os.path.join(current_base, folder_name)
                current_base = folder
            # Двигаемся назад
            else:
                folder = go_upper(current_base, (next * -1) + 1)
                folder = os.path.join(folder, folder_name)
                current_base = folder
            files.append(folder)
            previous_index = indent
        else:
            filename = strip_row
            files.append(os.path.join(current_base, filename))

    return files


def main(argv):
    if len(argv) - 1 != 1:
        # Можно добавить параметр force который бы "насильно" пересоздавал структуру проекта
        raise AttributeError("Неверные аргументы. Пример использования: python task_7_2.py [config_file.indent]")

    config_file = argv[1]

    if not os.path.exists(config_file):
        raise FileNotFoundError("Конфиг файл не найден")

    with open(config_file, 'r', encoding="utf-8") as file:
        # Тут можно обойтись и без readlines()
        result = config_to_dict(file.readlines())
        config_to_live(result)
        for filepath in result:
            print(os.path.relpath(filepath, os.getcwd()))


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))

"""
    my_project
    my_project\settings
    my_project\settings\__init__.py
    my_project\settings\dev.py
    my_project\settings\prod.py
    my_project\mainapp
    my_project\mainapp\templates
    my_project\mainapp\templates\mainapp
    my_project\mainapp\templates\mainapp\base.html
    my_project\mainapp\templates\mainapp\index.html
    my_project\mainapp
    my_project\mainapp\__init__.py
    my_project\mainapp\models.py
    my_project\mainapp\views.py
    my_project\mainapp
    my_project\mainapp\onemore_file_here.txt
    my_project\authapp
    my_project\authapp\__init__.py
    my_project\authapp\models.py
    my_project\authapp\views.py
    my_project\authapp\templates
    my_project\authapp\templates\authapp
    my_project\authapp\templates\authapp\base.html
    my_project\authapp\templates\authapp\index.html
    my_project\settings
    my_project\settings\settings_empty_folder
    my_project\settings\settings_empty_file.cfg
    my_project\settings\settings_empty_folder
    my_project\settings\settings_empty_folder\settings_empty_file.cfg
    
    Process finished with exit code 0

"""
