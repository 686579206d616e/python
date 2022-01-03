def thesaurus_adv(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений
    for name in args:
        family_chr = name.split(' ')[-1][0]
        name_chr = name[0]

        # Создать структуру под данные, try except
        if family_chr not in dict_out:
            dict_out[family_chr] = {}

        if name_chr not in dict_out[family_chr]:
            dict_out[family_chr][name_chr] = []

        # Добавить данные
        dict_out[family_chr][name_chr].append(name)

    # Сортировка
    return dict(sorted(dict_out.items()))


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

# check = "{'А': {'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'С': {" \
#         "'И': ['Иван Сергеев', 'Инна Серова'], 'А': ['Анна Савельева']}}"
# if check == str(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")):
#     print("check")
