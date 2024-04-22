"""
1. Напишите функцию для транспонирования матрицы
"""

# Вариант 1
#
# n = int(input('Введите количество строк в матрице: '))
# matrix = []
# for i in range(n):
#     matrix.append(input('Введите строку матрицы через запятую: ')
#                   .replace(' ', '')
#                   .split(','))
#
# if ~len(matrix):
#     matrix = None
#
#
# def transp(matrix=None):
#     if matrix is None:
#         matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     matrix_t = []
#     for i in range(len(matrix[0])):
#         lst_tmp = []
#         for j in range(len(matrix)):
#             lst_tmp.append(matrix[j][i])
#         matrix_t.append(lst_tmp)
#     return matrix_t
#
# if __name__ == '__main__':
#     print(trenspon(matrix))


# Вариант 2

import numpy as np

n = int(input('Введите количество строк в матрице: '))
matrix = []
for i in range(n):
    matrix.append(input('Введите строку матрицы через запятую: ')
                  .replace(' ', '')
                  .split(','))

if ~len(matrix):
    matrix = None


def trenspon(matrix=None):
    if matrix is None:
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return np.array(matrix).T


if __name__ == '__main__':
    print(trenspon(matrix))
