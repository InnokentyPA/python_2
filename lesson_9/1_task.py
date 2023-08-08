# ------------------------------------------- 1 -----------------------------
"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""

from typing import Callable


def secret_one(num: int, count: int) -> Callable[[], None]:
    def guess_num():
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

    return guess_num


if __name__ == '__main__':
    game = secret_one(42, 6)
    game()
