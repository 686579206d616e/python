class MyException(Exception):
    _default_detail: str = 'base error'

    def __init__(self, detail: str = None):
        if detail:
            self._default_detail = detail

    def __str__(self):
        return self._default_detail


class NumberChecking:
    def __init__(self):
        self.number_list = []
        self.while_continue = True

    def check_number(self):
        while self.while_continue:
            try:
                try:
                    user_input = int(input('Введите число: '))
                    is_continue = input(f'"{user_input}" добавлено. Прервать? (введите stop): ').lower().strip()
                    self.number_list.append(user_input)
                    if is_continue == 'stop':
                        print(self.number_list)
                        self.while_continue = False
                        break

                except ValueError:
                    raise MyException

            except MyException:
                is_continue = input(f"Это не число! Прервать? (введите stop): ").lower().strip()
                if is_continue == 'stop':
                    print(self.number_list)
                    self.while_continue = False
                    break
                else:
                    self.check_number()


a = NumberChecking()
a.check_number()