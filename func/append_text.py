import os


def append_text(name: str, text: str) -> None:
    if os.path.isfile(name):
        with open(name, 'a') as file:
            if file.tell() > 0:
                file.write('\n')
            file.write(text)
            print(f'Текст добавлен в файл {name}')

    else:
        print(f'Файл {name} не существует')

