# ------------------------------------------- 3 -----------------------------
"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст."""


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self.__age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age


p_1 = Person('Иванов', 'Иван', 'Иванович', 30)
print(p_1.full_name())
p_1.birthday()
print(p_1.get_age())
