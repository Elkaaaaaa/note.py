from os import path

from model.NoteEditor import NoteEditor


class Load(object):
    @staticmethod
    def load_csv():
        if path.exists("Note.csv"):
            with open("Note.csv", "r", encoding="UTF-8") as csv:
                notes = csv.readlines()
            n = 0
            for note in notes:
                note = note.split(";")
                NoteEditor.add(note[0], note[1])
                NoteEditor.notes[n].date = note[2].replace("\n", "")
                n += 1
            print("Заметки успешно извлечены!")

        else:
            print("Файла 'Note.csv' не существует")

    @staticmethod
    def load_json():
        if path.exists("Note.json"):
            with open("Note.json", "r", encoding="UTF-8") as json:
                notes = json.readlines()
            notes.pop(0)
            notes.pop(0)
            notes.pop(len(notes) - 1)
            notes.pop(len(notes) - 1)
            notes.pop(len(notes) - 1)
            temp_notes = []
            for i in range(len(notes)):
                note = notes[i].replace(
                    "{", "").replace(
                    "}", "").replace(
                    "\n", "").replace(
                    "\t", "").replace(
                    "[", "").replace(
                    "]", "")
                temp_notes.append(note.split())
            n = 0
            for i in range(0, len(temp_notes), 5):
                NoteEditor.add(temp_notes[i][2], temp_notes[i + 1][2])
                NoteEditor.notes[n].date = temp_notes[i + 2][2]
                n += 1
            print("Заметки успешно извлечены!")

        else:
            print("Файла 'Note.json' не существует")
