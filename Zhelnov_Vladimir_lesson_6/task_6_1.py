"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>) . Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""

from pprint import pprint


# 93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (
# 0.8.16~exp12ubuntu10.21)"
def get_ip_address(line: str) -> str:
    """ Получает из логов IP Адрес """
    # 255.255.255.255
    ip_end = line.find('-')
    if ip_end == -1:
        return

    result = line[0:ip_end].split(' ')
    return result[0]


def get_http_uri(line: str) -> list:
    """ Получает метод запроса, путь запроса, и версию HTTP """
    offset = line.find('"') + 1
    offset_end = line.find('"', offset)
    return line[offset:offset_end].split(' ')


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    result = None
    if len(line) > 0:
        result = (get_ip_address(line), get_http_uri(line)[0], get_http_uri(line)[1])  # Ваша реализация здесь
    return result  # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    # pass  # передавайте данные в функцию и наполняйте список list_out кортежами
    for row in fr:
        list_out.append(get_parse_attrs(row))

pprint(list_out)
# pprint(list_out.__len__())
