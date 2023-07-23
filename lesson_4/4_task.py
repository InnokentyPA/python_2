# ------------------------------------------- 4 -----------------------------
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без
# использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def list_sort(my_list: list) -> None:
    for j in range(len(my_list) - 1):
        for i in range(len(my_list) - 1 - j):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

some_list = [330, 5, 1, 8, 2, 10, 12, 120]
print(some_list)
list_sort(some_list)
print(some_list)
