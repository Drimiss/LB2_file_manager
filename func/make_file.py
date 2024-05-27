def make_file(files):

    for name in files:
        my_file = open(name, "w")
        my_file.close()
        print(f'Файл {name} создан')