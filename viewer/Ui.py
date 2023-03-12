from _import.Load import Load
from export.Save import Save
from model.NoteEditor import NoteEditor


class Ui(object):

    @staticmethod
    def main_menu():  # Модель главного меню
        while True:
            print("Выберете список действий:"
                  "\n\t1. Создать заметку"
                  "\n\t2. Посмотреть список заметок"
                  "\n\t3. Сохранить заметки"
                  "\n\t4. Загрузить заметки"
                  "\n\t0. Выход")
            key = input_numbs_int("---> ")
            if key == 1:
                title = input("Введите заголовок заметки:  ")
                msg = input("Введите заметку: ")
                NoteEditor.add(title, msg)
            elif key == 2:
                if len(NoteEditor.notes) != 0:
                    while True:
                        NoteEditor.print()
                        print("Выберете действие: "
                              "\n\t1. Редакировать Заметку"
                              "\n\t2. Сортировать Заметки"
                              "\n\t3. Удалить Заметку"
                              "\n\t0. Отмена")
                        key = input_numbs_int("--->")
                        if key == 1:
                            while True:
                                key = input_numbs_int("Выберете заметку\n\t0. Отмена\n--->")
                                if key == 0:
                                    break
                                if key <= len(NoteEditor.notes):
                                    print("Заголовок заметки: " +
                                          str(NoteEditor.notes[key - 1].title) +
                                          "\nВведите новый Заголовок: ")
                                    title = input("--->")
                                    print("Текст заметки: " +
                                          str(NoteEditor.notes[key - 1].msg) +
                                          "\nВведите новый текст: ")
                                    msg = input("--->")
                                    NoteEditor.edit(key, title, msg)
                                    break
                                else:
                                    print("Такой заметки нет!")
                        elif key == 2:
                            while True:
                                print("Выберете параметр сортировки: "
                                      "\n\t1. По дате ↑"
                                      "\n\t2. По дате ↓"
                                      "\n\t3. По заголовку ↑"
                                      "\n\t4. По заголовку ↓"
                                      "\n\t0. Отмена")
                                key = input_numbs_int("--->")
                                if key == 0:
                                    break
                                if 5 > key > 0:
                                    NoteEditor.sort(key)
                                    break
                                else:
                                    print("Такого действия нет!")
                        elif key == 3:
                            while True:
                                key = input_numbs_int("Выберете заметку\n\t0. Отмена\n--->")
                                if key == 0:
                                    break
                                if key <= len(NoteEditor.notes):
                                    NoteEditor.dell(key)
                                    break
                        elif key == 0:
                            break
                        else:
                            print("Такого действия нет")

                else:
                    print("Заметок нет :(\n")
            elif key == 3:
                if len(NoteEditor.notes) != 0:
                    while True:
                        print("Выберете формат: "
                              "\n\t1. csv"
                              "\n\t2. json"
                              "\n\t0. Отмена")
                        key = input_numbs_int("--->")
                        if key == 1:
                            Save.save_as_csv()
                            break
                        elif key == 2:
                            Save.save_as_json()
                            break
                        elif key == 0:
                            break
                        else:
                            print("Такого действия нет!")
                else:
                    print("Заметок нет :(\n")
            elif key == 4:
                while True:
                    print("Выберете формат: "
                          "\n\t1. csv"
                          "\n\t2. json"
                          "\n\t0. Отмена")
                    key = input_numbs_int("--->")
                    if key == 1:
                        Load.load_csv()
                        break
                    elif key == 2:
                        Load.load_json()
                        break
                    else:
                        print("Такого действия нет!")
            elif key == 0:
                print("Несохраненные заметки будут потеряны навсегда. Вы уверены?"
                      "\n\t1. Выйти"
                      "\n\t2. Отмена")
                while True:
                    key = input_numbs_int("--->")
                    if key == 1:
                        return
                    elif key == 2:
                        break
                    else:
                        print("Такого действия нет")
            else:
                print("Такого действия нет!")


def input_numbs_int(input_text):  # Функция ввода данных типа int
    while True:
        try:
            return int(input(f"{input_text}"))
        except ValueError:
            print("Введите корректное число")
