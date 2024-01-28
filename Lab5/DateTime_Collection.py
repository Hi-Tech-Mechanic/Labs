# Программирование на языке высокого уровня (Python).
# Задание №5 Вариант !!!
#
# Выполнил: Минатуллаев Р.Ш.
# Группа: ПИН-б-з-21-1
# E-mail: ruslan.minatullaev-1000@yandex.ru

import json
from DateTime_Methods import DateTime

class Collection:
    def __init__(self):
        self.__data = []

    def __getitem__(self):
        pass

    def add(self, value):
        self.__data.append(value)
    
    def remove(self, index):
        self.__data.pop(index)

    def save(self):
        data = {"collection": self.get_data()}
        with open("data.json", "w") as file:
            json.dump(json.dumps(data, default=class_to_dict), file)
        print("Данные сохранены: {}".format(self.get_data()))

    def load(self):
        with open("data.json", "r") as file:
            json.load(file)
        print("Данные загружены: {}".format(self.get_data()))

    def get_data(self):
        return [component for component in self.__data]

def class_to_dict(obj):
    return obj.__dict__