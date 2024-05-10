"""
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в
конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно
работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
"""

import os

directory = 'files'
def rename_files(file_name_out,
                  len_num_out,
                  extension_in,
                  extension_out,
                  len_name_in):

    counter = 0

    for f in os.listdir(directory):
        file_name_in = f.split('.')[0]
        file_extension_in = f.split('.')[-1]

        # проверяем, что файл нужного расширения
        if file_extension_in == extension_in:
            # создаем счетчик файлов нужной длины
            zeros_len = len_num_out - len(str(counter))
            count_name = '0' * zeros_len + str(counter)

            # создаем новое имя файла
            name_slice = file_name_in[len_name_in[0]:len_name_in[1]]
            new_file_name = '' + name_slice + '_' + file_name_out + '_' + count_name + '.' + extension_out
            counter += 1

            # переименовываем
            os.rename(f'{directory}/{f}',
                      f'{directory}/{new_file_name}')


if __name__ == '__main__':
    rename_files('new_file',
                 3,
                 'doc',
                 'docx',
                 [2, 4])