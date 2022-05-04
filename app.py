import database

user_choice = """
- a to add books
- l to list all books
- r to mark a book as read
- d to delete a book
- q to quit : 
"""


def prompt_add_book():
    name = input('Name : ').lower()
    author = input('Author: ').lower()
    database.add_book(name, author)


def prompt_list_books():
    database.list_books()


def prompt_read_book():
    name = input("Enter name of book to mark as 'read': ")
    database.mark_as_read(name)


def prompt_delete_book():
    name = input("Enter name of book to delete: ")
    database.delete_book(name)


def unknown():
    print("Unknown command")


selection = {'a': prompt_add_book,
             'l': prompt_list_books,
             'r': prompt_read_book,
             'd': prompt_delete_book}


def menu():

    while True:
        user_input = input(user_choice)
        if user_input == 'q':
            print('Quitting ...')
            break
        if user_input not in ['a', 'l', 'r', 'd']:
            print("Unknown command")
        else:
            selection[user_input]()




menu()

