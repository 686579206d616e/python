# С учетом того что все имена в capitalize()
def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений

    for name in args:
        if name[0] not in dict_out:
            dict_out[name[0]] = []

        dict_out[name[0]].append(name)

    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
