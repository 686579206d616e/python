import time

class TrafficLight:

    def __init__(self):
        self.__color = 'красный'
        self.__index_color = 0
        self.__timings = 0

    def __how_much(self):
        """ Сколько секунд """
        seconds = (4, 2, 3)
        return seconds[TrafficLight.__icolor(self.__color)]

    @staticmethod
    def __icolor(color):
        """ Индекс цвета, надо Enum изучить """
        if color == 'красный':
            return 0
        elif color == 'жёлтый':
            return 1
        elif color == 'зелёный':
            return 2

    def __switch_next(self):
        """ Переключение цвета """
        switcher = ('жёлтый', 'зелёный', 'красный')
        old_color = self.__color
        self.__color = switcher[TrafficLight.__icolor(self.__color)]
        self.__icolor = TrafficLight.__icolor(self.__color)
        print(f"Переключился свет: ({old_color.upper()}) на {self.__color}, {self.__timings} сек")

    def running(self):
        """ Процессинг тика  """
        print(f"Начальный цвет: {self.__color}")
        while True:

            self.__timings += 1
            time.sleep(1)

            print(f"Тик {self.__timings}")

            if self.__timings >= self.__how_much():
                self.__switch_next()
                self.__timings = 0


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()

"""
Начальный цвет: красный
Тик 1
Тик 2
Тик 3
Тик 4
Переключился свет: (КРАСНЫЙ) на жёлтый, 4 сек
Тик 1
Тик 2
Переключился свет: (ЖЁЛТЫЙ) на зелёный, 2 сек
Тик 1
Тик 2
Тик 3
Переключился свет: (ЗЕЛЁНЫЙ) на красный, 3 сек

"""