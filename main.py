import the_smart_guy as sg
import ya_uploader as ya
import stackoverflow as st

from pprint import pprint



if __name__ == '__main__':

# Task_1
# Нужно определить кто самый умный(intelligence) из трех супергероев - Hulk, Captain America, Thanos.
    print('Solution_1')
    TOKEN = '2619421814940190'
    names = ['Hulk', 'Captain America', 'Thanos']
    names2 = ['Spider-man', 'Venom', 'Carnage']
    print(sg.show_the_smart_guy(sg.get_intelligence(TOKEN, names)))
    print(sg.show_the_smart_guy(sg.get_intelligence(TOKEN, names2)))

# Task_2
# Нужно написать программу, которая принимает на вход путь до файла на компьютере
# и сохраняет на Яндекс.Диск с таким же именем.

# Создание папки опционально. Если не вызывать метод .create_dir('имя папки'),
# и не указывать имя папки в методе .upload(file_name, 'имя папки'),
# то файл загрузится на диск в папку 'Files'.
    print('Solution_2')
    uploader = ya.YaUploader('Ваш TOKEN')
    new_dir = uploader.create_dir('имя папки')
    result = uploader.upload('имя файла') # <- 'имя папки'
    print(new_dir)
    print(result)

# Task_3
# Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг 'Python'.
    print('Solution_3')
    pprint(st.get_questions("python", 2))