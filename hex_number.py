# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата

number = int(input('Введите число '))

change = format(number, '#x')
print(change)
if hex(number) == change:
    print('1')
else:
    print('0')