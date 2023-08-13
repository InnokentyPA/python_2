# ------------------------------------------- 4 -----------------------------
"""
Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
    ○ шестизначный идентификационный номер
    ○ уровень доступа вычисляемый как остаток от деления
      суммы цифр id на семь
"""


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id_num: int):
        super().__init__(last_name, first_name, patronymic, age)
        if id_num < 100_000 or id_num > 999_999:
            self.id_num = randint(100000, 999999)
        else:
            self.id_num = id_num

    def set_level(self):
        s = sum(num for num in str(self.id_num))
        return s % self.MAX_LEVEL


bobby = Employee('Smit', 'Jon', 'Leo', 33, 89)
print(f'{bobby.id_num = }')
print(f'{bobby.set_level() = }')
