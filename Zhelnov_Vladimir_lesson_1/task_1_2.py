def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    result = 0
    for x in dataset:
        if x % 7 == 0:
            result += x
    return result  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    # dataset2 = [x + 17 for x in dataset]
    for idx, x in enumerate(dataset):
        dataset[idx] += 17
    return sum_list_1(dataset)  # Верните значение полученной суммы


# Создать список, состоящий из кубов нечётных чисел от 1 до 1000
my_list = list(filter(None, [x ** 3 if x % 2 != 0 else None for x in range(1, 1001)]))
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
