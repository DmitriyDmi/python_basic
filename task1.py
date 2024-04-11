"""
2. Напишите программу, которая получает целое число и
возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

num16_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
OSNOVANIE = 16


def task1():
    num10 = int(input('Введите число: '))
    num_iter = num10 // OSNOVANIE
    num16 = ''

    if num_iter == 0:
        ost = num10
        if ost in num16_dict:
            ost = num16_dict[ost]
        num16 += str(ost)
    else:
        num_iter = num10
        while num_iter > 0:
            ost = num_iter % OSNOVANIE
            num_iter = num_iter // OSNOVANIE
            if ost in num16_dict:
                ost = num16_dict[ost]
            num16 += str(ost)
    print(f'Проверка hex(): {hex(num10)}')
    return print(f'Наш ответ: {num16[::-1]}')


if __name__ == '__main__':
    task1()