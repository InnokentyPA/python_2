# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

one = 1
two = 2
nine = 9
ten = 10
hundred = 100
thousand = 1000

while True:
    number = int(input("Введите число от 1 до 999: "))

    if one <= number <= nine:
        result = f"Введена цифра. Квадрат числа: {number ** two}"
    elif ten <= number < hundred:
        digit_1 = number // ten
        digit_2 = number % ten
        result = f"Введено двузначное число. Произведение цифр: {digit_1 * digit_2}"

    elif hundred <= number < thousand:
        result = f"Введено трехзначное число. Зеркальное отображение: {int(str(number)[::-one])}"

    else:
        print("Введено число вне диапазона от 1 до 999. Попробуйте снова.")
        continue

    print(result)
    break
