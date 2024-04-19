"""
4. Создайте словарь со списком вещей для похода в
качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

max_weight = int(input('Введите максимальную грузоподьемность: '))
item_in_bag = []
item_dict = {
    'Палатка': 15,
    'Еда': 3,
    'Лопата': 5,
    'Топор': 4,
    'Одежда': 6,
    'Посуда': 1,
    'Гитара': 3
}
sorted_dict = dict(sorted(item_dict.items(), key=lambda item: item[1], reverse=True))

for i in sorted_dict:
    if max_weight >= sorted_dict[i]:
        item_in_bag.append(i)
        max_weight -= sorted_dict[i]
print(item_in_bag)