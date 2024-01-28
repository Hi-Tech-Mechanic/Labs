# Программирование на языке высокого уровня (Python).
# Задание №5 Вариант !!!
#
# Выполнил: Минатуллаев Р.Ш.
# Группа: ПИН-б-з-21-1
# E-mail: ruslan.minatullaev-1000@yandex.ru

from datetime import datetime

class Ticket:
    def __init__(self, number_of_trips, expiration_date, personal_data):
        self.number_of_trips = number_of_trips
        self.expiration_date = expiration_date
        self.__personal_data = personal_data

    def check_ticket(self):
        if (self.number_of_trips > 0 and self.expiration_date > get_current_date_INT()):
            return True
        else: return False

    def spend_trip(self):
        self.number_of_trips -= 1
        print("1 поездка истрачена, осталось: {}".format(self.get_remainder_trips()))

    def get_remainder_trips(self):
        return self.number_of_trips

    def get_remainder_time(self, value):
        return self.expiration_date - value

class UnlimitedTicket(Ticket):
    def __init__(self, expiration_date, personal_data):
        self.expiration_date = expiration_date
        self.personal_data = personal_data

    def check_ticket(self):
        if (self.expiration_date > get_current_date_INT()):
            return True
        else: return False

    def spend_trip(self):
        print("1 поездка истрачена, осталось: {}".format(self.get_remainder_trips()))

    def get_remainder_trips(self):
        return "бесконечно"

class TripsLimitedTicket(Ticket):
    MAX_TRIP_COUNT = 3;
    def __init__(self, number_of_trips, personal_data):
        self.number_of_trips = number_of_trips
        self.personal_data = personal_data
        if (self.number_of_trips > self.MAX_TRIP_COUNT):
            self.number_of_trips = self.MAX_TRIP_COUNT

    def check_ticket(self):
        if (self.number_of_trips > 0):
            return True
        else: return False

    def get_remainder_time(self, value):
        return "билет бессрочный"

def get_current_date_INT():
    return datetime.toordinal(datetime.today())