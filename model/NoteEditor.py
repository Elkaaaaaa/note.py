from _operator import attrgetter

from model.Note import Note


class NoteEditor(object):
    notes = []

    @staticmethod
    def add(title, msg):
        NoteEditor.notes.append((Note(title, msg)))

    @staticmethod
    def dell(i):
        if i <= len(NoteEditor.notes):
            NoteEditor.notes.pop(i - 1)

    @staticmethod
    def edit(i, title, msg):
        if i <= len(NoteEditor.notes):
            NoteEditor.notes.pop(i - 1)
            NoteEditor.notes.insert(i - 1, (Note(title, msg)))

    @staticmethod
    def print():
        for i in range(len(NoteEditor.notes)):
            j = i + 1
            print(str(j) + ". " + str(NoteEditor.notes[i].title) + ": " + str(NoteEditor.notes[i].date) + "\n\t" + str(
                NoteEditor.notes[i].msg))
        print()

    @staticmethod
    def sort(index):
        if index == 1:
            return NoteEditor.notes.sort(key=attrgetter("date"))
        elif index == 2:
            NoteEditor.notes.sort(key=attrgetter("date"))
            return NoteEditor.notes.reverse()
        elif index == 3:
            return NoteEditor.notes.sort(key=attrgetter("title"))
        elif index == 4:
            NoteEditor.notes.sort(key=attrgetter("title"))
            return NoteEditor.notes.reverse()
