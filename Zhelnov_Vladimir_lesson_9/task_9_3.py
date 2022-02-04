class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        # Ваш код здесь
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income  # {wage, bonus}


class Position(Worker):

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f"{self.name} {self.surname}"

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        return self.income['wage'] + self.income['bonus']


if __name__ == '__main__':
    welder = Position('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})
    driver = Position('петр', 'николаев', 'водитель', {'wage': 30000, 'bonus': 7500})
    scientist = Position('геннадий', 'разумов', 'ученый', {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(), welder.get_total_income())  # Иван Васильев 65000
    print(driver.get_full_name(), driver.get_total_income())  # Петр Николаев 37500
    print(scientist.get_full_name(), scientist.get_total_income())  # Геннадий Разумов 175000

"""
иван васильев 65000
петр николаев 37500
геннадий разумов 175000
"""