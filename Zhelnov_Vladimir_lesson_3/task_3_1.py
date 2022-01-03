def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    translate_words = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    russian_words = ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')
    str_out = 'None'  # так как требует str вывод функция

    if value in translate_words:
        str_out = russian_words[translate_words.index(value)]

    return str_out


print(num_translate("one"))
print(num_translate("two"))
print(num_translate("three"))
print(num_translate("four"))
print(num_translate("five"))
print(num_translate("six"))
print(num_translate("seven"))
print(num_translate("eight"))
print(num_translate("nine"))
print(num_translate("ten"))
print(num_translate("eleven"))
