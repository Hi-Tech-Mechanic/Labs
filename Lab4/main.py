# Программирование на языке высокого уровня (Python).
# Задание №5 Вариант !!!
#
# Выполнил: Минатуллаев Р.Ш.
# Группа: ПИН-б-з-21-1
# E-mail: ruslan.minatullaev-1000@yandex.ru

from DateTime_Methods import DateTime
from DateTime_Methods import MoonTime
from DateTime_Methods import open_sample_class

###################################################
obj = DateTime([2024, 1, 24], [13, 58])
#get_date = decorator(obj.get_date)

"Вывод и работа с методами"
obj.display_all_attributes()
obj.current_datetime()
obj.set_date([2077, 1, 24])
obj.set_time([10, 15])
obj.display_all_attributes()
print(obj)

"Сохранение и загрузка"
obj.save()
obj.load()
###################################################
obj_2 = MoonTime(obj.get_time(), obj.get_date())
obj_3 = obj_2
print("\n"*3,obj_2)

"Перерузка операторов"
tmp_1 = open_sample_class(10)
tmp_2 = open_sample_class(50)
print(tmp_1 + tmp_2)
print(tmp_1 - tmp_2)
print(tmp_1 * tmp_2)
print(tmp_1 / tmp_2)
print(tmp_1 // tmp_2)
###################################################