# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.

start_row = 2
end_row = 9
start_column = 2
end_column = 10

for i in range(2, 11):
    for j in range(2, 6):
        print(f"{j} x {i} = {j * i}\t", end="")
    print("\t", end="")
    for j in range(6, 10):
        print(f"{j} x {i} = {j * i}\t", end="")
    print()