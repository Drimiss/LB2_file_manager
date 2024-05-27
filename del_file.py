import os

def del_files(files):

    for name in files:
        if os.path.isfile(name):
            os.remove(name)
            print(f'Файл {name} успешно удален')
        
        else:
            os.remove(name)
            print(f'Файл {name} успешно удален')