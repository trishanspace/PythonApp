import Repository.exportDataFromFile as exf
import Repository.importDataToFile as imf
import Models.note

def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Models.note.note(title=title, body=body)
    array_notes = exf.read_file()
    for i in array_notes:
        if Models.note.note.get_id(note) == Models.note.note.get_id(i):
            Models.note.note.set_id(note)
    array_notes.append(note)
    imf.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")

def show(txt):
    array_notes = exf.read_file()

    if array_notes:
        if txt == "all":
            print("Журнал заметок:")
            for i in array_notes:
                print(Models.note.note.map_note(i))

        elif txt == "id":
            for i in array_notes:
                print("id: ", Models.note.note.get_id(i))
            id = input("\nВведите id заметки: ")
            flag = True
            for i in array_notes:
                if id == Models.note.note.get_id(i):
                    print(Models.note.note.map_note(i))
                    flag = False
            if flag:
                print("Такого id нет")

        elif txt == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(Models.note.note.get_date(i))
                if date == date_note[:10]:
                    print(Models.note.note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой!")

def del_notes():
    id = input("Введите id для удаления: ")
    array_notes = exf.read_file()
    flag = False

    for i in array_notes:
        if id == Models.note.note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        imf.write_file(array_notes, 'a')
        print("Заметка с id: ", id, " удалена!")
    else:
        print("Такого id нет")

def change_note():
    id = input("Введите id изменяемой заметки: ")
    array_notes = exf.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Models.note.note.get_id(i):
            i.title = input("измените  заголовок:\n")
            i.body = input("измените  описание:\n")
            Models.note.note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        imf.write_file(array_notes_new, 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("нет такого id")