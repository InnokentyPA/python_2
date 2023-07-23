# ------------------------------------------- 8 -----------------------------
# Создайте несколько переменных заканчивающихся и не оканчивающихся на 's'.
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def replace_globals():
    my_dict = globals()
    print(globals())
    add_dict = {}
    for key, value in my_dict.items():
        if (len(key) > 1) and (key[-1] == 's'):
            add_dict[key[:-1]] = value
            my_dict[key] = None

    my_dict.update(add_dict)

datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

replace_globals()
print(globals())
