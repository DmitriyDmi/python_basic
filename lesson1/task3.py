"""
4. Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

lower_limit = 0
upper_limit = 1000
num = randint(lower_limit, upper_limit)
tryes = 10 # Попытки

def task3(tryes, num, lower_limit, upper_limit):
    print()

    if tryes == 0:
        return print('К сожалению попыток не осталось')

    print(f'Загаданое число от {lower_limit} до {upper_limit}')
    your_num = int(input('Угадайте загаданное число: '))

    if lower_limit > your_num or upper_limit <  your_num:
        print('Попытка не засчитана, попробуйте еще раз')
        return task3(tryes, num, lower_limit, upper_limit)

    if your_num == num:
        return print('Поздравляет! Вы угадали')

    if your_num < num:
        print('Загаданное число больше вашего')
        lower_limit = your_num
        tryes -= 1
        print(f'У вас осталось {tryes} попыток')
        return task3(tryes, num, lower_limit, upper_limit)

    if your_num > num:
        print('Загаданное число меньше вашего')
        upper_limit = your_num
        tryes -= 1
        print(f'У вас осталось {tryes} попыток')
        return task3(tryes, num, lower_limit, upper_limit)


if __name__ == '__main__':
    task3(tryes, num, lower_limit, upper_limit)