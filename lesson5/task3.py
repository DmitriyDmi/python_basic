"""
4. Создайте функцию генератор чисел Фибоначчи
"""

n = int(input('Введите до какого числа нужно число Фибоначи: '))


def fibonachi(n):
    return [fibonachi(i-1) + fibonachi(i-2) if i > 1 else 1 if i == 1 else 0 for i in range(n + 1)][-1]


if __name__ == '__main__':
    print(f'Число Фибоначи для {n} равно {fibonachi(n)}')
