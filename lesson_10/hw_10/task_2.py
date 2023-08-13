# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра. 


import time


class ATM:
    TAX_LOWER_BOUND, TAX_UPPER_BOUND = 30, 600
    WEALTH_BOUND = 5_000_000
    TAKE_OFF_TAX_RATE = 1.5 / 100
    REFINANCE_RATE = 3.0 / 100
    WEALTH_TAX_RATE = 10 / 100
    LCM = 50
    Q = 3
    M1 = 25_000_000_000_000

    def __init__(self, prec=35):
        self.sum_ = 0
        self.operations_counter = 0
        self.exit_flag = False
        self.locked = False

    def take_off(self, amount_of_money: int) -> bool:
        if not self.valid(amount_of_money):
            print(f'amount_of_money must be divisible by {ATM.LCM}')
            return False
        elif amount_of_money > self.sum_:
            print(f'amount_of_money is too high')
            return False
        self.operations_counter += 1
        tax = amount_of_money * ATM.TAKE_OFF_TAX_RATE
        if tax < ATM.TAX_LOWER_BOUND:
            tax = ATM.TAX_LOWER_BOUND
        elif tax > ATM.TAX_UPPER_BOUND:
            tax = ATM.TAX_UPPER_BOUND
        if amount_of_money + tax > self.sum_:
            print(f'cannot process the common taxation')
            return False
        taxable_amount = 0
        if self.wealth:
            taxable_amount = amount_of_money if self.sum_ - amount_of_money >= ATM.WEALTH_BOUND \
                else self.sum_ - ATM.WEALTH_BOUND
        wealth_tax = taxable_amount * ATM.WEALTH_TAX_RATE
        if (amount := amount_of_money + tax + wealth_tax) > self.sum_:
            print(f'cannot process the wealth-taxation')
            return False
        self.sum_ -= amount
        print(f'{self}')
        return True

    def pay_in(self, amount_of_money: int) -> bool:
        if not self.valid(amount_of_money):
            print(f'amount_of_money must be divisible by {ATM.LCM}')
            return False
        self.operations_counter += 1
        amount = amount_of_money * (1 - ATM.WEALTH_TAX_RATE) if self.wealth else amount_of_money
        self.sum_ += amount
        if self.third_op:
            self.sum_ += amount_of_money * ATM.REFINANCE_RATE
        if self.cheater:
            print(f"Now you have all the world's money or even more! Sweet dreams are made of this...")
            while True:
                time.sleep(1)
                print(f'You are UNDER ARREST, DO NOT MOVE, police officers are about to come...')
        print(f'{self}')
        return True

    @property
    def wealth(self) -> bool:
        return self.sum_ > ATM.WEALTH_BOUND

    @property
    def third_op(self) -> bool:
        return self.operations_counter % ATM.Q == 0

    @property
    def cheater(self) -> bool:
        return self.sum_ > ATM.M1

    @staticmethod
    def valid(amount: int) -> bool:
        return amount % ATM.LCM == 0

    def __str__(self):
        return f'account money: {self.sum_}'

    def __repr__(self):
        return str(self)

    def exit(self) -> None:
        self.exit_flag = True
        print(f'Session aborted, account money: {self.sum_}')


def input_valid_num(message: str) -> int:
    string = input(message)
    if string.isdigit() and (num := int(string)) > 0:
        return num
    else:
        print(f'Enter a natural number!..')
        input_valid_num(message)


# ATM-interaction:
def main():
    atm = ATM(prec=36)
    # core cycle:
    while not atm.exit_flag:
        command = input(f'Enter your request: ')
        match command:
            case 'take off':
                amount = input_valid_num(f'Enter an amount of money to be taken off: ')
                if not atm.take_off(amount):
                    print(f'Invalid operation!')
            case 'pay in':
                amount = input_valid_num(f'Enter an amount of money to be put: ')
                if not atm.pay_in(amount):
                    print(f'Invalid operation!')
            case 'exit':
                atm.exit()
                break
            case _:
                print(f'Enter a valid request: '
                      f"'take off', 'pay in' or 'exit'")


main()