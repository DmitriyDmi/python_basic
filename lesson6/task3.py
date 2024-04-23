from task2 import eight_queens
from task2 import random_position


def correct_positions():
    count = 0
    correct_positions_list = []
    while count < 4:
        trys_list = [] # список уже проверенных координат
        positions = random_position()
        positions_set = set(map(str, positions)) # делаем из координат множество, чтоб не сравнивать индексы
        if positions_set not in trys_list: # если координаты еще не проверяли
            trys_list.append(positions_set)
            queens_variant = eight_queens(positions) # для непроверенных координат запуск проверку задачи ферзей
            if queens_variant:
                count += 1
                correct_positions_list.append(queens_variant)
    return correct_positions_list


if __name__ == '__main__':
    print(*correct_positions(), sep='\n')
# output
# (True, [[1, 3], [2, 6], [3, 8], [4, 2], [5, 4], [6, 1], [7, 7], [8, 5]])
# (True, [[1, 4], [2, 7], [3, 5], [4, 3], [5, 1], [6, 6], [7, 8], [8, 2]])
# (True, [[1, 6], [2, 2], [3, 7], [4, 1], [5, 4], [6, 8], [7, 5], [8, 3]])
# (True, [[1, 6], [2, 3], [3, 5], [4, 8], [5, 1], [6, 4], [7, 2], [8, 7]])