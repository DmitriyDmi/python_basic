"""
2. Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def function(**kwargs):
    dict1 ={}
    for name, value in kwargs.items():
        try:
            hash(value)
        except:
            value = str(value)
        dict1[value] = name
    return dict1


if __name__ == '__main__':
    print(function(a=[2,5], b=2, c=3))
    #output {'[2, 5]': 'a', 2: 'b', 3: 'c'}
