import Note


def create_note():
    title = input('Enter note title: ')
    body = input('En4ter note body:: ')
    return Note.Note(title=title, body=body)


def menu():
    print("\nThe Notes app welcomes you! \nChoose an action\n1 - View notes\n2 - Add note\n3 - Delete notes\n4 - Edit note\n5 - Filter by date\n6 - Filter by id\n7 - Exit\n\nEnter choice: ")