# from sys import getsizeof


def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    normal_word = value.strip().lower()
    str_out = 'None'  # default так как требует str вывод функция
    translate_words = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    # print(getsizeof(translate_words), 'bytes')

    # Избежать исключения, try except
    if normal_word in translate_words:
        index = translate_words.index(normal_word) + 1
    else:
        return str_out

    # Switch case
    if index is not None:
        if index == 1:
            str_out = 'один'
        elif index == 2:
            str_out = 'два'
        elif index == 3:
            str_out = 'три'
        elif index == 4:
            str_out = 'четыре'
        elif index == 5:
            str_out = 'пять'
        elif index == 6:
            str_out = 'шесть'
        elif index == 7:
            str_out = 'семь'
        elif index == 8:
            str_out = 'восемь'
        elif index == 9:
            str_out = 'девять'
        elif index == 10:
            str_out = 'десять'

    return str_out.capitalize() if value[0].isupper() else str_out


print(num_translate_adv("One"))
print(num_translate_adv("two"))
print(num_translate_adv("Three"))
print(num_translate_adv("four"))
print(num_translate_adv("Five"))
print(num_translate_adv("six"))
print(num_translate_adv("Seven"))
print(num_translate_adv("eight"))
print(num_translate_adv("nine"))
print(num_translate_adv("Ten"))
print(num_translate_adv("eleven"))
print(num_translate_adv("One "))
