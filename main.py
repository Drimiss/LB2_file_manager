from func.append_text import append_text
from func.cat_file import cat_file
from func.copy_files import copy_files
from func.del_dir import remove_dir
from func.del_file import del_files
from func.make_dir import make_dir
from func.make_file import make_file
from func.move_files import move_files
from func.rename_file import rename_file
import os


def main():
    print('Вы запустили простой файловый менеджер, введите число от 0 до 10 чтобы выбрать одну из опций:')
    os.mkdir('working_folder')
    folder = 'working_folder'

    while True:

        print('\n1) Создание папки (с указанием имени)')
        print('2) Удаление папки по имени')
        print('3) Перемещение между папками (в пределах рабочей папки)')
        print('4) Создание пустых файлов с указанием имени')
        print('5) Запись текста в файл')
        print('6) Просмотр содержимого текстового файла')
        print('7) Удаление файлов по имени')
        print('8) Копирование файлов из одной папки в другую')
        print('9) Перемещение файлов')
        print('10) Переименование файлов')
        print('0) Завершение работы\n')
        print(f'Вы находитесь в папке {folder}\n')

        integer = int(input('Введите число от 0 до 10: '))
        while integer > 10 or integer < 0:
            integer = int(input('Введите число от 0 до 10: '))


        match integer:
            case 0:
                print('Спасибо, что воспользовались нашим файловым менеджером!')
                break

            case 1:
                dir_name = input('Введите название папки: ')
                make_dir(os.path.join(folder, dir_name))

            case 2:
                dir_name = input('Введите название папки: ')
                remove_dir(os.path.join(folder, dir_name))

            case 3:
                dir_name = input('Введите название папки: ')

                if dir_name == '':
                    folder = 'working_folder'

                elif dir_name == '..':

                    if not os.path.samefile(folder, os.path.abspath('working_folder')):
                        folder = os.path.dirname(folder)
                    else:
                        print('Вы не можете перейти выше рабочей папки.')


                else:
                    if os.path.isdir(os.path.join(folder, dir_name)):
                        folder = os.path.join(folder, dir_name)

            case 4:
                file_name = input('Введите название файлов через запятую: ').split(',')
                file_name = [os.path.join(folder, file) for file in file_name]
                make_file(file_name)

            case 5:
                file_name = input('Введите название файла: ')
                text = input('Введите текст для добавления: ')
                append_text(os.path.join(folder, file_name), text)

            case 6:
                file_name = input('Введите название файла: ')
                cat_file(os.path.join(folder, file_name))

            case 7:
                file_name = input('Введите название файлов через запятую: ').split(',')
                file_name = [os.path.join(folder, file) for file in file_name]
                del_files(file_name)

            case 8:
                dir1 = input('Введите путь к исходной папке: ')
                dir2 = input('Введите путь к папке, куда нужно скопировать: ')
                files = input('Введите название файлов через запятую: ').split(',')
                files = [os.path.join(folder, file) for file in files]
                copy_files(os.path.join(folder, dir1), os.path.join(folder, dir2), files)

            case 9:
                dir1 = input('Введите путь к исходной папке: ')
                dir2 = input('Введите путь к папке, куда нужно скопировать: ')
                files = input('Введите название файлов через запятую: ').split(',')
                files = [os.path.join(folder, file) for file in files]
                move_files(os.path.join(folder, dir1), os.path.join(folder, dir2), files)

            case 10:
                first_name = input('Введите текущее имя файла: ')
                second_name = input('Введите новое имя файла: ')
                rename_file(os.path.join(folder, first_name), os.path.join(folder, second_name))


if __name__ == "__main__":
    main()