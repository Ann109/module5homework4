# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию
from random import choice
class Building:  #  создали класс
        total = 0  #  с атрибутом total
        def __init__(self):  #  создали инициализатор для класса билдинг который будет увеличивать атрибут тотал на один
                Building.total += 1
                self.name = choice(["кирпичный", "панельный", "каменный", "блочный", "керамический", "деревянный", "монолитный"])
                self.type = choice(["таунхаус", "апартаменты", "коттедж", "вилла", "особняк", "дворец", "жилой комлекс"])
                self.build_list = {self.name: self.type}
for i in list(range(40)):
    a = Building()
    print(a.total, a.build_list)


