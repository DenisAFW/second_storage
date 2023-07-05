# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.
import fractions

N1 = input('Введите число 1 ')
N2 = input('Введите число 2 ')
N3 = input('Введите число 3 ')
N4 = input('Введите число 4 ')
print(f'Введены числа {N1}/{N2} и {N3}/{N4}')

number_multi_1 = number_sum_1 = int(N1)
number_multi_2 = number_sum_2 = int(N2)
number_multi_3 = number_sum_3 = int(N3)
number_multi_4 = number_sum_4 = int(N4)
# Сумма дробей

if number_sum_2 != number_sum_4:
    number_sum_2 *= number_sum_4
    number_sum_4 = number_sum_2
    number_sum_1 *= int(N4)
    number_sum_3 *= int(N2)

sum_numerator = number_sum_1 + number_sum_3
count = 2
while count < sum_numerator:
    if sum_numerator % count != 0:
        count += 1
    elif number_sum_4 % count != 0:
        count += 1
    else:
        break
numerator = sum_numerator // count
divider = number_sum_4 // count

if numerator == divider:
    print('Сумма дробей равна 1')
else:
    print(f'Сумма дробей равна {numerator}/{divider}')

# Произведение дробей
multiplication_numerator = number_multi_1 * number_multi_3
multiplication_divider = number_multi_2 * number_multi_4

count = multiplication_numerator - 1
while count != 0:
    if multiplication_numerator % count != 0:
        count -= 1
    elif multiplication_divider % count != 0:
        count -= 1
    else:
        break

print(f'Произведение дробей равно {multiplication_numerator // count}/{multiplication_divider // count}')

first_fraction = fractions.Fraction(int(N1), int(N2))
second_fraction = fractions.Fraction(int(N3), int(N4))
print(f'\nСумма дробей равна {first_fraction + second_fraction}')
print(f'Произведение дробей равно {first_fraction * second_fraction}')
