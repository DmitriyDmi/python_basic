"""
2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def split_path(text):
    text = text.replace('\\', '/')
    path = text[::-1].split('/', 1)[1][::-1]
    file = text[::-1].split('/', 1)[0][::-1]
    file_name = file.split('.')[0]
    app = file.split('.')[1]
    return (path, file_name, app)


text = 'https://github.com/DmitriyDmi/python_basic/blob/main/lesson4/task3.py'
text2 = r'C:\Users\р\python_lessons\5\task1.py'

if __name__ == '__main__':
    print(split_path(text))
    print(split_path(text2))
# output
# ('https://github.com/DmitriyDmi/python_basic/blob/main/lesson4', 'task3', 'py')
# ('C:/Users/р/python_lessons/5', 'task1', 'py')
