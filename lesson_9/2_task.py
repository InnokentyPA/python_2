# ------------------------------------------- 2 -----------------------------
"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные
в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""

from random import randint
from typing import Callable


def check_param(func: Callable) -> Callable[[int, int], None]:
    def wrapper(*args):
        if not args[0] in range(1, 101) or not args[1] in range(1, 11):
            return func(randint(1, 100), randint(1, 10))
        return func(*args)

    return wrapper


@check_param
def guess_num(num: int, count: int):
    secret = randint(1, num)
    print(f"Угадайте число от 1 до {num}. У вас {count} попыток.")

    for attempt in range(count):
        guess = int(input(f"Попытка №{attempt + 1}: "))

        if guess < secret:
            print("Загаданное число больше.")
        elif guess > secret:
            print("Загаданное число меньше.")
        else:
            print("Поздравляю! Вы угадали число!")
            break


if __name__ == '__main__':
    guess_num(420, 60)
