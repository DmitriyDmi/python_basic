"""
3. Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

import random
def eight_queens(position_list=None):
    n = 8
    x = []
    y = []
    if position_list is None: # ручной ввод координат
        for i in range(n):
            new_x, new_y = [int(s) for s in input().split()]
            x.append(new_x)
            y.append(new_y)
    else:  # получение функцией списка координат
        if len(position_list) == n: # проверка корректности списка
            for position in position_list:
                x.append(position[0])
                y.append(position[1])
        else:
            return False

    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

    if correct:
        if position_list is None: # если был ручной ввод координат
            position_list = [] # генерируем список координат из списков x y
            for i in zip(x, y):
                position_list.append(list(i))
        return True, position_list
    else:
        return False


def random_position(): # генерируем список координат
    position_list = []
    while len(position_list) < 8:
        x = len(position_list) + 1 # на каждую линию по 1 ферзю, а то перебор сочетаний 8 по 64 это много(4 426 165 368)
        y = random.randint(1, 8) # а так бутет 8^8 вариантов = 16 777 216, в почти в 300раз меньше
        if [x, y] not in position_list: # проверка, что нет одинаковых координат
            position_list.append([x, y]) # хотя их и так не будет, х везде разный
    return position_list


if __name__ == '__main__':
    print(eight_queens())
