def transform_string(number: int) -> str:
    postfix = 'ов' if 10 < number % 100 < 20 else 'а' if 1 < number % 10 < 5 else 'ов' if number % 10 != 1 else ''
    return "{} процент{}".format(number, postfix)


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
