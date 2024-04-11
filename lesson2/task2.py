"""
3. Напишите программу, которая принимает две строки
вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""

import fractions


def task2():
    str1 = input('Введите строку 1 вида a/b : ')
    str2 = input('Введите строку 2 вида a/b : ')
    x1, y1 = int(str1.split('/')[0]), int(str1.split('/')[1])
    x2, y2 = int(str2.split('/')[0]), int(str2.split('/')[1])
    summa = str((x1 * y2 + x2 * y1)) + '/' + str((y1 * y2))
    multipl = str((x1 * x2)) + '/' + str((y1 * y2))
    print(f'Сумма дробей: {summa}')
    print(f'Умножение дробей: {multipl}')
    print()
    print('Проверка fractions:')
    f1 = fractions.Fraction(x1, y1)
    f2 = fractions.Fraction(x2, y2)
    print(f'Сумма дробей: {f1 + f2}')
    print(f'Умножение дробей: {f1 * f2}')


if __name__ == '__main__':
    task2()