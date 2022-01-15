import requests
import datetime


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


def currency_rates(code: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_text = response.text
    offset = response.text.find(code)
    if offset == -1:
        return None
    cur_value = currency_value(response_text, offset)
    return cur_value
