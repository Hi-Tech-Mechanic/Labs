# Программирование на языке высокого уровня (Python).
# Задание №5 Вариант !!!
#
# Выполнил: Минатуллаев Р.Ш.
# Группа: ПИН-б-з-21-1
# E-mail: ruslan.minatullaev-1000@yandex.ru

from datetime import datetime
import json

def decorator(func):
    #return '<decorator>', func, '</decorator>'
    decor = "{}{}".format(("#"), func) #"#"*20),"\n"
    return decor


class DateTime:
    def __init__(self, date, time):
        self.__date = date;
        self.__time = time;

    def __str__(self):
        message = "Дата:{}\t||\tВремя:{}".format(str(self.__date), str(self.__time))
        return message

    def __add__(self, other):
        return ("$"*100)

    def current_datetime(self):
        print("Текущее время:", datetime.now())

    #@decorator
    def get_date(self):
        return ([element for element in self.__date]);

    #@decorator
    def get_time(self):
        return ([element for element in self.__time]);

    def set_date(self, value):
        self.__date = value;

    def set_time(self, value):
        self.__time = value;

    def display_all_attributes(self):
        print("Дата:", self.get_date())
        print("Время:", self.get_time())

    def save(self):
        data = {"time": self.__time, "date": self.__date}
        with open("data.json", "w") as file:
            json.dump(data, file)
        print("Данные сохранены:", self.get_time(), "\t", self.get_date())

    def load(self):
        with open("data.json", "r") as file:
            json.load(file)
        print("Данные загружены:", self.get_time(), "\t", self.get_date())

class MoonTime(DateTime):
    def __init__(self, time, date):
        self.__time = time
        self.__date = date

    def __str__(self):
        return("{indent}Дата и время на луне:\n{indent_2}Дата:{date}\tВремя:{time}"
               .format(date = self.get_time(), time = self.get_date(), indent="\t"*3, indent_2="\t"*2))

    def get_time(self):
        return [round(element / 2, 2) for element in self.__time]

    def get_date(self):
        return [round(element / 2, 2) for element in self.__date]

class open_sample_class(DateTime):
    def __init__(self, value):
        self.field = value
        
    def __sub__(self, other):
        return ("{} - вычитание".format(self.field - other.field))

    def __mul__(self, other):
        return ("{} - умножение".format(self.field * other.field))

    def __floordiv__(self, other):
        return ("{} - деление".format(self.field / other.field))

    def __truediv__(self, other):
        return ("{} - деление на цело".format(self.field // other.field))