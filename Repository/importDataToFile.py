import Models.note


def write_file(array, mode):
    file = open("notepad.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notepad.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Models.note.note.to_string(notes))
        file.write('\n')
    file.close