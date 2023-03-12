from model.NoteEditor import NoteEditor


class Save(object):

    @staticmethod
    def save_as_csv():
        with open("Note.csv", "w", encoding="UTF-8") as csv:
            for i in range(len(NoteEditor.notes)):
                csv.writelines(str(NoteEditor.notes[i].title) + ";" + str(NoteEditor.notes[i].msg) + ";" + str(
                    NoteEditor.notes[i].date + "\n"))

    @staticmethod
    def save_as_json():
        with open("Note.json", "w", encoding="UTF-8") as json:
            json.write('{"Notes" : [\n')
            for i in range(len(NoteEditor.notes)):
                json.write('\t{\n')
                json.write(f'\t\t"title" : "{NoteEditor.notes[i].title}",\n')
                json.write(f'\t\t"message" : "{NoteEditor.notes[i].msg}",\n')
                json.write(f'\t\t"date" : "{NoteEditor.notes[i].date}"\n')
                if i < len(NoteEditor.notes) - 1:
                    json.write('\t},\n')
                else:
                    json.write('\t}\n')
            json.write('\t]\n}')
