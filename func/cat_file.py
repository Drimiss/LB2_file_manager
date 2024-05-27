import os


def cat_file(name: str) -> None:
    if os.path.isfile(name):
        with open(name, 'r') as file:
            print(f'Содержимое файла {name}:')
            print(file.read())

    else:
        print(f'Файл {name} не существует')


