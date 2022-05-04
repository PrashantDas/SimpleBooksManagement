import json
import os


file_name = "books_json.json"


def get_all_books():
    with open(file_name, 'r') as fread:
        return json.load(fread)


def _save_all_books(data):  # name includes a preceding underscore to ward of evil programmers
    with open(file_name, 'w') as fwrite:
        json.dump(data, fwrite)
    print("The database was updated")


def add_book(name, author):
    new_book = {'name': name, 'author': author, 'read': False}
    if file_name not in os.listdir():
        with open(file_name, 'w') as fhand:
            json.dump({"books_dict": [new_book]}, fhand)  # a dictionary with key books_dict & value which is a list is dumped
        print(f"{name} written to json")
    else:
        contents = get_all_books()  # this is a dictionary
        contents["books_dict"].append(new_book)
        _save_all_books(contents)


def mark_as_read(name):
    if file_name not in os.listdir():
        print("Database does not exist")
    else:
        contents = get_all_books()  # this is a dictionary
        for book in contents["books_dict"]:
            if book['name'] == name:
                book['read'] = True
                _save_all_books(contents)
                break
        else:
            print(f"{name} does not exist in the database")


def list_books():
    contents = get_all_books()  # this is a dictionary
    print(format('NAME', '>14s'), format('AUTHOR', '>14s'), format('READ-STATUS', '>14s'))
    for book in contents["books_dict"]:
        print(format(f"{book['name'].title()}", '>14s'),
              format(f"{book['author'].title()}", '>14s'),
              format(f"{book['read']}", '>14s'))


def delete_book(name):
    contents = get_all_books()  # this is a dictionary
    contents['books_dict'] = [book for book in contents["books_dict"] if book['name'] != name]
    _save_all_books(contents)
    print(f"{name} was deleted")







