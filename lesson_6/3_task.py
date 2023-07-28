# ------------------------------------------- 3 -----------------------------
# Улучшаем задачу 2. Добавьте возможность запуска
# функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов:
# параметры вызова функции. Для преобразования строковых
# аргументов командной строки в числовые
# параметры используйте генераторное выражение.

from random import randint
from sys import argv


def guess(lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    number = randint(lower, upper)
    for _ in range(count):
        answer = int(input(f'Введите число между [{lower}, {upper}]: '))
        if answer < number:
            print(f'Число {answer} меньше загаданного')
        elif answer > number:
            print(f'Число {answer} больше загаданного')
        else:
            return True
    return False


if __name__ == '__main__':
    name, *param = argv
    print(guess(*(int(n) for n in param)))
