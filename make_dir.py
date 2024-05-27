import os

def make_dir(name):
    
    try:
        os.mkdir(name)
        print(f'Папка {name} создана')
    
    except FileExistsError:
        print(f'Папка {name} уже существует')