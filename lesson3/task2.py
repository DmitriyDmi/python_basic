"""
3. В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

import re

new_str = input().lower()
new_str = re.sub(r'[^\w\s]', '', new_str)
new_lst = new_str.split()
new_dict = {}
for i in new_lst:
    if i not in new_dict:
        new_dict[i] = 0
    new_dict[i] += 1

sorted_dict = sorted(new_dict.items(), key=lambda item: item[1], reverse=True)
print()
print(sorted_dict[:10])