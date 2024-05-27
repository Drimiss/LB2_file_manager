import os


def make_dir(name: str) -> None:
    try:
        os.mkdir(name)
        print(f'Папка {name} создана')
    except FileExistsError:
        print(f'Папка {name} уже существует')

