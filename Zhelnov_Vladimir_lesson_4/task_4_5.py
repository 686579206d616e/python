import utils


def main(argv):
    try:
        currency_value, currency_date = utils.currency_rates_adv(argv[1])
        if currency_value is None:
            result = "К сожалению данный валюты не существует, попробуйте гонконский доллар: HKD"
        else:
            result = "%s, %s" % (currency_value, currency_date)
    except IndexError:
        result = "Вы не указали валюту. Пример использования: python task_4_5.py USD"
    return result


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
