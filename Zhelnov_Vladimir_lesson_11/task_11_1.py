from datetime import datetime


class Date:
    date_str: str = "empty"

    def __init__(self, date_str: str):
        """ Class Date - принимает строчку формата день-месяц-год"""
        Date.date_str = date_str

    @classmethod
    def extract_num(cls):
        """ Извлекает день месяц год в числе """
        # должен извлекать число, месяц, год и преобразовывать их тип к типу «Число»
        date = Date.valid_str(cls.date_str)
        if date:
            return int(f"{date.day}{date.month}{date.year}")

    @staticmethod
    def valid_str(date_str: str) -> datetime:
        """ Валидация даты, None - явно не валидно"""
        # должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12)
        try:
            return datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            return


print(Date('08-02-2022').extract_num())  # 822022
print(Date.valid_str('08-02-2022'))  # 2022-02-08 00:00:00 - Valid
print(Date.valid_str('08-13-2022'))  # None - Not valid
print(Date('08-13-2022').extract_num())  # None

"""
    822022
    2022-02-08 00:00:00
    None
    None
"""