# Программирование на языке высокого уровня (Python).
# Задание №5 Вариант !!!
#
# Выполнил: Минатуллаев Р.Ш.
# Группа: ПИН-б-з-21-1
# E-mail: ruslan.minatullaev-1000@yandex.ru

import time
from tickets import Ticket
from tickets import UnlimitedTicket
from tickets import TripsLimitedTicket

class Person:
    def drive(self, ticket):
        if isinstance(ticket, TripsLimitedTicket):
            print("Использован билет с ограниченными поездками")
        elif isinstance(ticket, UnlimitedTicket):
            print("Использован безлимитный билет")
        elif isinstance(ticket, Ticket):
            print("Использован обычный билет")

        if ticket.check_ticket():
            ticket.spend_trip()
            time.sleep(1)
            print("Вы сели на транспорт")
            time.sleep(1)
            print("Поездка началась")
        else: raise ValueError("Запас поездок недостаточен, либо прошел срок давности")