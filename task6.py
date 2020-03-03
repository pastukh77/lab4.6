from notebook import Note, Notebook


def class_note():
    note = Note('We are the champions ', tags="Champion's note")
    print('This object represents a class:', type(note), '\n',)
    print("All attributes are Note object: ", note.__dict__, '\n')
    print('Also it has such atributes: ', dir(note))


def class_notebook():
    notebook = Notebook()
    note = Note('We are the champions ', tags="Champion's note")
    print('This object represents a class:', type(note), '\n', )
    print("All attributes are Notebook object: ", note.__dict__, '\n')
    print('Also it has such atributes: ', dir(note))

if __name__ == '__main__':
    class_note()
    print('\n')
    class_notebook()



