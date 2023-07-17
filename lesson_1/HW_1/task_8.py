# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

one = 1
two = 2
rows = int(input("Сколько рядов у ёлки? "))

for i in range(one, rows + one):
    print(" " * (rows - i) + "*" * (two * i - one))
