"""
$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
"""

import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'^([0-9\w]+)@(\w+)\.(\w+)$')
    search = RE_MAIL.search(email)
    if search:
        groups = search.groups()
        return {'username': groups[0], 'domain': "%s.%s" % (groups[1], groups[2])}
    raise ValueError('wrong email: %s' % (email))


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('somASDSAe@geekbrains.ru'))
    print(email_parse('someo4ne2@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))

"""
{'username': 'someone', 'domain': 'geekbrains.ru'}
{'username': 'somASDSAe', 'domain': 'geekbrains.ru'}
{'username': 'someo4ne2', 'domain': 'geekbrains.ru'}
Traceback (most recent call last):
    raise ValueError('wrong email: %s' % (email))
ValueError: wrong email: someone@geekbrainsru
"""