import requests

"""

- Можно ли, используя только методы класса str, решить поставленную задачу?
Ответ: Да

- Eсть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Да, здесь важна математическая точность

- Сильно ли усложняется код функции при этом?
Нет

"""

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_text = response.text

    offset = response.text.find(code)
    # Если текст не найден - возвращает None
    if offset == -1:
        return None

    # Определяем смещение относительно названия
    offset_nominal = response.text.find('<Value>', offset) + 7
    nominal_str = ''

    # Мы знаем что максимальная длина курса валюты 7 символов
    # Собираем по-символьно курс валюты
    for i in range(0, 7):
        nominal_char = response_text[i + offset_nominal]
        # Если символ является числом
        if nominal_char.isnumeric():
            nominal_str += nominal_char
        # Если это символ запятая то добавляем точку
        # Чтобы избежать проблем с конвертацией float()
        elif nominal_char == ',':
            nominal_str += '.'

    result_value = float(nominal_str)
    return result_value


print(currency_rates("USD"))
print(currency_rates("HKD"))
print(currency_rates("noname"))