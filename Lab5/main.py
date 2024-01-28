# Программирование на языке высокого уровня (Python).
# Задание №5 Вариант !!!
#
# Выполнил: Минатуллаев Р.Ш.
# Группа: ПИН-б-з-21-1
# E-mail: ruslan.minatullaev-1000@yandex.ru

from DateTime_Collection import Collection 
from DateTime_Methods import DateTime

if __name__ == "__main__":
    tmp = DateTime()
    new_collection = Collection()

    new_collection.add(tmp)
    new_collection.save()
    new_collection.load()
    print(new_collection.get_data())
    new_collection.remove(0)
    print(new_collection.get_data())

    ############################################
    for i in range(0, 10):
        new_collection.add(tmp)
        new_collection.save()
        new_collection.load()
        print(new_collection.get_data())

