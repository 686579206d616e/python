"""
Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя 
обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
"""


def main(argv):
    if len(argv) - 1 != 2:
        raise TypeError("Неверные аргументы. Пример использования: python task_6_5.py hobby.csv users.csv")

    try:
        with open('users_hobby.txt', 'w', encoding='utf-8') as fw:
            with open(argv[2], 'r', encoding='utf-8') as user_file:
                with open(argv[1], 'r', encoding='utf-8') as hobby_file:
                    for user in user_file:
                        fw.write("%s: %s\n" % (user.rstrip(), hobby_file.readline().rstrip()))

        print("Файл успешно сохранен: %s" % ('users_hobby.txt'))

    except FileNotFoundError:
        raise FileNotFoundError("Проверьте наличие файлов: %s %s" % (argv[1], argv[2]))


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))

