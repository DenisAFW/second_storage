# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

choice = 0
money = 10000
count = 0
print('Добро пожаловать в банкомат')
while choice != 3:
    print('Введите номер желаемой операции:')
    print('1 - пополнение счета,')
    print('2 - снятие суммы,')
    print('3 - выход')
    count += 1
    choice = int(input('Введите номер операции '))

    if count % 3 == 0:
        refill = money * 0.03
        money += refill
        count = 0
        print(f'ы {count}')
        print(
            f'Вы выполнили 3 операции, за это вам начислены 3% от общей сумму равные {money}, процент равен {refill}')

    if choice == 1:
        print(f'Текущая сумма на счете - {money}')
        if money > 5000000:
            tax = money * 0.1
            money -= tax
            print(f'Произведены вычеты из суммы в размере {tax}, текущая сумма на счете - {money}, соболезную, ваш банк')

        input_money = int(input('Введите сумму пополнения счета, вводимая сумма должна быть кратна 50 у.е. '))

        if input_money % 50 == 0:
            write_on = input_money * 0.015
            if write_on < 30:
                write_on = 30
                input_money -= write_on
                money += input_money
                print(f'Счет пополненен на сумму {input_money}, процент за операцию {write_on}')
                print(f'Текущее состояние счета - {money}')
            elif write_on > 600:
                write_on = 600
                input_money -= write_on
                money += input_money
                print(f'Счет пополненен на сумму {input_money}, процент за операцию {write_on}')
                print(f'Текущее состояние счета - {money}')
            else:
                input_money -= write_on
                money += input_money
                print(f'Счет пополненен на сумму {input_money}, процент за операцию {write_on}')
                print(f'Текущее состояние счета - {money}')
        else:
            print('Введена неверная сумма')

    elif choice == 2:
        print(f'Текущая сумма на счете - {money}')
        if money > 5000000:
            tax = money * 0.1
            money -= tax
            print(f'Произведены вычеты из суммы в размере {tax}, текущая сумма на счете - {money}, соболезную, ваш банк')

        output_money = int(input('Введите сумму снятия со счета, вводимая сумма должна быть кратна 50 у.е. '))

        if output_money % 50 == 0:
            write_off = output_money * 0.015  # ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
            if output_money < money:
                if write_off < 30:
                    write_off = 30
                    output_money -= write_off
                    money -= output_money
                    print(f'Вы сняли со счета {output_money}, процент за операцию {write_off}')
                    print(f'Текущее состояние счета - {money}')
                elif write_off > 600:
                    write_off = 600
                    output_money -= write_off
                    money -= output_money
                    print(f'Вы сняли со счета {output_money}, процент за операцию {write_off}')
                    print(f'Текущее состояние счета - {money}')
                else:
                    output_money -= write_off
                    money -= output_money
                    print(f'Вы сняли со счета {output_money}, процент за операцию {write_off}')
                    print(f'Текущее состояние счета - {money}')
            else:
                print(f'Указанная сумма {output_money} превышает сумму на счете {money}!')
        else:
            print('Введена неверная сумма')

    elif choice == 3:
        print('Спасибо за пользование нашим банком!')
