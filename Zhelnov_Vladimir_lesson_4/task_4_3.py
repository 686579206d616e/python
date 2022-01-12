import datetime
import requests


def currency_value(response: str, offset: int) -> float:
    """ Возвращает значение курса валюты """
    offset_nominal = response.find('<Value>', offset) + 7
    nominal_str = ''

    for i in range(0, 7):
        nominal_char = response[i + offset_nominal]
        if nominal_char.isnumeric():
            nominal_str += nominal_char
        elif nominal_char == ',':
            nominal_str += '.'

    result_value = float(nominal_str)
    return result_value


def currency_rates_adv(code: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_text = response.text
    response_date = response.headers.get('Date')

    offset = response.text.find(code)
    if offset == -1:
        return None, None

    cur_value = currency_value(response_text, offset)
    cur_date = datetime.datetime.strptime(response_date, '%a, %d %b %Y %H:%M:%S %Z')

    return cur_value, cur_date.date()


kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)
