def main(argv):
    if len(argv) - 1 != 1:
        raise AttributeError("Неверные аргументы. Пример использования: python add_sale.py [Сумма]")

    with open('bakery.csv', 'a+', encoding='utf-8') as fw:
        line_string = "%s\n" % (argv[1].ljust(20))
        # print(len(line_string)) 21
        if len(line_string) > 20:
            fw.write(line_string)
        else:
            raise ValueError("Вы ввели слишком большое число")


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
