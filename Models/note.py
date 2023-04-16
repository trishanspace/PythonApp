from datetime import datetime
import uuid
import Controller.count as counter


class note:
    def __init__(self, id=str(counter.counter()), title="текст", body="текст",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(note):
        return note.id

    def set_id(note):
        note.id = str(counter.counter())

    def get_title(note):
        return note.title

    def set_title(note):
        note.title = note

    def get_body(note):
        return note.body

    def set_body(note):
        note.body = note

    def get_date(note):
        return note.date

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nid: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date