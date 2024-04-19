"""
2. Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst_dupl = input().split()
lst_tmp = []
total_lst = []
for i in lst_dupl:
    if i not in lst_tmp:
        lst_tmp.append(i)
    else:
        if i not in total_lst:
            total_lst.append(i)

print(total_lst)