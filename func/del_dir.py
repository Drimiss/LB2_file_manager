import os


def remove_dir(name: str) -> None:
    try:
        os.rmdir(name)
        print(f'Папка {name} удалена!️')
    except FileNotFoundError:
        print(f'Папки {name} не существует')
    except OSError as e:
        print(f'Не удалось удалить папку {name}, папка не пустая')

