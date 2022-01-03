from random import randint, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]  # len(5)
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]  # len(5)
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]  # len(5)


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = []
    for x in range(0, count):
        list_out.append("%s %s %s" % (nouns[randint(0, len(nouns) - 1)],
                                      adverbs[randint(0, len(adverbs) - 1)],
                                      adjectives[randint(0, len(adjectives) - 1)]))
    return list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, repeat: bool = False) -> list:
    """Возвращает список шуток в количестве count, repeat запрет на повторы"""

    # Если надо повторяться, используем уже имеющуюся функцию
    if repeat is True:
        return get_jokes(count)

    # Возращаем сообщение что нельзя создать список так как не хватает элементов
    if count > len(nouns) or count > len(adverbs) or count > len(adjectives):
        return ["Невозможно создать список, не хватает исходных данных"]

    list_out = []
    exclude_parts = [[], [], []]
    for x in range(0, count):
        # Генерация индексов для шуток
        parts = (choice([i for i in range(0, len(nouns)) if i not in exclude_parts[0]]),
                 choice([i for i in range(0, len(adverbs)) if i not in exclude_parts[1]]),
                 choice([i for i in range(0, len(adjectives)) if i not in exclude_parts[2]]))

        # Добавляем исключения шуток в память
        # Можно было здесь добавить исключение repeat, без повторного использования старой функции
        for i in range(0, 3):
            exclude_parts[i].append(parts[i])

        # Приводим к нужному формату
        list_out.append("%s %s %s" % (nouns[parts[0]], adverbs[parts[1]], adjectives[parts[2]]))

    return list_out


# Вариативность "принтов"
print('Без повторов, 2 шутки: ', get_jokes_adv(2))
print('Без повторов, 5 шуток: %s' % (get_jokes_adv(5)))
print('Ошибка:', get_jokes_adv(6)[0])
print(get_jokes_adv(count=10, repeat=True))  # Разрешаем повторение
print(get_jokes_adv(6, repeat=True))  # Разрешаем повторение
