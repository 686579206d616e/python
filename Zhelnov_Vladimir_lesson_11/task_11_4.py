# Начать работу над проектом Склад оргтехники.
#
# Создать класс, описывающий склад. А также класс Оргтехника, который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (Принтер, Сканер, Ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:

    def __init__(self):
        self._items = {'Общее': [], 'Отдел 2': [], 'Отдел 3': [], 'Отдел К': []}

    def add(self, item, category:str = "Общее"):
        try:
            self._items[category].append(item)
        except:
            print("Указан неверный отдел при добавлении")

    def show(self):
        print(self._items)

    def input(self):
        try:
            office_type = int(input(f'Что необходимо добавить? (0-Принтер, 1-Сканер, 2-Ксерокс):'))
            if 0 <= office_type <= 2:
                office_name = input(f'Введите ярлык для оборудования? (Например: Осторожно! Бьет током!):')
                object = None

                if office_type == 0:
                    object = Printer(office_name)
                elif office_type == 1:
                    object = Scaner(office_name)
                elif office_type == 2:
                    object = Xerox(office_name)

                self.add(object)

                is_continue = input(f'Добавить еще? (Нажмите Enter - Да, либо напишите Выйти):')
                if is_continue == '':
                    self.input()
                else:
                    print(self._items)

            else:
                self.input()
        except ValueError:
            self.input()


class OfficeEquipment:

    def __init__(self, name: str = "", weight: float = 10.0, height: float = 10.0):
        """ Оснащение офиса """
        self.name = name
        self.weight = weight
        self.height = height

    def __str__(self):
        return f"<{self.__class__.__name__}[{self.name}][{self.weight} кг][{self.height} см]>"


class Printer(OfficeEquipment):
    def __init__(self, name: str = "Принтер", print_speed: float = 666.0):
        super().__init__(name)
        self.print_speed = print_speed


class Scaner(OfficeEquipment):
    def __init__(self, name: str = "Сканер", scan_speed: float = 666.0):
        super().__init__(name)
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):
    def __init__(self, name: str = "Ксерокс", xerox_speed: float = 666.0):
        super().__init__(name)
        self.xerox_speed = xerox_speed


printer = Printer("Принтер Пети")
print(printer)
scaner = Scaner("Сканер Васи")
print(scaner)
xerox = Xerox("Ксерокс Натальи")
print(xerox)

storage = Storage()
# По-умолчанию добавляет в Общее
storage.add(printer)
storage.add(scaner, "Отдел К")
storage.add(xerox, "Отдел 2")
storage.show()

# Добавляем всё в общее так как офис только переехал,
# отсортируем по отделам позже
storage.input()

"""
<Printer[Принтер Пети][10.0 кг][10.0 см]>
<Scaner[Сканер Васи][10.0 кг][10.0 см]>
<Xerox[Ксерокс Натальи][10.0 кг][10.0 см]>

{'Общее': [<__main__.Printer object at 0x000001E15DCF9BB0>], 'Отдел 2': [<__main__.Xerox object at 0x000001E15DCF86A0>], 
'Отдел 3': [], 'Отдел К': [<__main__.Scaner object at 0x000001E15DCF9B50>]}

Что необходимо добавить? (0-Принтер, 1-Сканер, 2-Ксерокс):2

Введите ярлык для оборудования? (Например: Осторожно! Бьет током!):Бьет!

Добавить еще? (Нажмите Enter - Да, либо напишите Выйти):

Что необходимо добавить? (0-Принтер, 1-Сканер, 2-Ксерокс):0

Введите ярлык для оборудования? (Например: Осторожно! Бьет током!):Принтует!

Добавить еще? (Нажмите Enter - Да, либо напишите Выйти):Выйти

{'Общее': [<__main__.Printer object at 0x000001E15DCF9BB0>, <__main__.Xerox object at 0x000001E15DCF85E0>, 
<__main__.Printer object at 0x000001E15DCF8580>], 'Отдел 2': [<__main__.Xerox object at 0x000001E15DCF86A0>], 
'Отдел 3': [], 'Отдел К': [<__main__.Scaner object at 0x000001E15DCF9B50>]}


"""