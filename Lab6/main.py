# Программирование на языке высокого уровня (Python).
# Задание №5 Вариант !!!
#
# Выполнил: Минатуллаев Р.Ш.
# Группа: ПИН-б-з-21-1
# E-mail: ruslan.minatullaev-1000@yandex.ru

from datetime import datetime
from person import Person
from tickets import Ticket
from tickets import UnlimitedTicket
from tickets import TripsLimitedTicket
from tickets import get_current_date_INT

if __name__ == "__main__":
    TICKET_VALIDITY_TIME = get_current_date_INT() + 30

    client = Person()
    averageTicket = Ticket(2, TICKET_VALIDITY_TIME, "Tady")
    unlimitedTicket = UnlimitedTicket((TICKET_VALIDITY_TIME + 50), "Jack")
    limitedTicket_1 = TripsLimitedTicket(50, "Mary")

    client.drive(averageTicket)
    print("Дней до окончания билета: {}\n\n".format
        (averageTicket.get_remainder_time(get_current_date_INT())))
    client.drive(unlimitedTicket)
    print("Дней до окончания билета: {}\n\n".format
        (unlimitedTicket.get_remainder_time(get_current_date_INT())))
    client.drive(limitedTicket_1)
    print("Дней до окончания билета: {}\n\n".format
          (limitedTicket_1.get_remainder_time(get_current_date_INT())))