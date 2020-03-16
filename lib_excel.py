import pandas as pd
from prettytable import PrettyTable


def show_catalog():
    with pd.ExcelFile("lib.xlsx") as xls:
        df = pd.read_excel(xls, usecols=['name', 'author', 'year', 'genre'])
    col = [i for i in df.columns]
    rows = []
    for i in df.index:
        for j in df.iloc[i]:
            rows.append(j)
    table = PrettyTable(col)
    while rows:
        table.add_row(rows[:len(col)])
        rows = rows[len(col):]
    print(table)


def input_redact():
    with pd.ExcelFile("lib.xlsx") as xls:
        df = pd.read_excel(xls, usecols=['name', 'author', 'year', 'genre'])
    print(df['name'])
    valid = False
    while not valid:
        redact_data = input('ENTER BOOK NAME FOR REDACT\n')
        if len(redact_data) == 0:
            print('ERROR\n')
            continue
        else:
            valid = True
        redact_data = redact_data.strip()
        replace(df, redact_data)


def replace(catalog, redact_name):
    counter = 0
    valid = False
    key = 0
    for k in catalog.index:
        for i in catalog.iloc[k]:
            j = str(i)
            j = j.lower()
            if j == redact_name.lower():
                key = k
                counter += 1
                print(f'\n{catalog.iloc[k]}\n')
    while not valid:
        enter_action = int(input(
            "1 - NAME\n"
            "2 - AUTHOR\n"
            "3 - YEAR\n"
            "4 - GENRE\n"
            "0 - EXIT IN MAIN MENU\n"
            "ENTER YOUR ACTION: \n"))
        try:
            enter_action = int(enter_action)
        except ValueError:
            print("ERROR\n")
            continue
        if enter_action == 1:
            redact_name = input("ENTER NEW BOOK NAME\n")
            redact_name = redact_name.strip()
            redact_name = redact_name.title()
            catalog.loc[key, 'name'] = redact_name
        elif enter_action == 2:
            redact_author = input("ENTER NEW AUTHOR BOOK\n")
            redact_author = redact_author.strip()
            redact_author = redact_author.title()
            catalog.loc[key, 'author'] = redact_author
        elif enter_action == 3:
            redact_year = input("ENTER NEW YEAR BOOK\n")
            redact_year = redact_year.strip()
            redact_year = redact_year.title()
            catalog.loc[key, 'year'] = redact_year
        elif enter_action == 4:
            redact_genre = input("ENTER NEW GENRE BOOK\n")
            redact_genre = redact_genre.strip()
            redact_genre = redact_genre.title()
            catalog.loc[key]['genre'] = redact_genre
        elif enter_action == 0:
            valid = True
        else:
            print("ERROR\n")
            continue
    if counter == 0:
        print('BOOK IS NOT IN CATALOG\n')
    else:
        with pd.ExcelWriter("lib.xlsx") as writer:
            catalog.to_excel(writer)


def add_book():
    with pd.ExcelFile("lib.xlsx") as xls:
        df = pd.read_excel(xls, usecols=['name', 'author', 'year', 'genre'])
    valid = False
    while not valid:
        new_book_data = input('ENTER NAME, AUTHOR, YEAR, GENRE SEPARATE BY COMMA?\n')
        new_book_data = new_book_data.split(',')
        if len(new_book_data) != 4:
            print('ERROR\n')
            continue
        new_book_data = list(map(lambda x: x.strip(), new_book_data))
        new_book_data = list(map(lambda x: x.title(), new_book_data))
        name_book = new_book_data[0]
        author_book = new_book_data[1]
        year_book = new_book_data[2]
        genre_book = new_book_data[3]
        counter = 0
        for i in df['name']:
            if i.lower() == name_book.lower():
                counter += 1
        if counter != 0:
            print('BOOK IS IN CATALOG\n')
            continue
        else:
            valid = True
        add(df, name_book, author_book, year_book, genre_book)


def add(catalog, name=None, author=None, year=None, genre=None):
    df = pd.DataFrame({
        'name': [name],
        'author': [author],
        'year': [year],
        'genre': [genre]}, index=[len(catalog.index)])
    result = catalog.append(df)
    with pd.ExcelWriter("lib.xlsx") as writer:
        result.to_excel(writer)
    print('BOOK ADDED\n')


def delete_book():
    with pd.ExcelFile("lib.xlsx") as xls:
        df = pd.read_excel(xls, usecols=['name', 'author', 'year', 'genre'])
    print(df['name'])
    valid = False
    while not valid:
        book_delete = input('ENTER BOOK NAME FOR DELETE:\n')
        if len(book_delete) == 0:
            print('ERROR\n')
            continue
        else:
            valid = True
        book_delete = book_delete.strip()
        delete(df, book_delete)


def delete(catalog, del_name):
    counter = 0
    for k in catalog.index:
        for i in catalog.iloc[k]:
            j = str(i)
            j = j.lower()
            if j == del_name.lower():
                counter += 1
                print(f'\n{catalog.iloc[k]}\n')
                print('DELETE BOOK: \n' '1 - YES\n' '2 - NOT\n')
                action_for_delete = int(input())
                try:
                    action_for_delete = int(action_for_delete)
                except ValueError:
                    print("ERROR\n")
                    continue
                if action_for_delete == 1:
                    catalog1 = catalog.drop([k])
                    catalog1.index = [i for i in range(len(catalog1.index))]
                    print('BOOK DELETED\n')
                    with pd.ExcelWriter("lib.xlsx") as writer:
                        catalog1.to_excel(writer)
                else:
                    print('EXIT')
    if counter == 0:
        print('BOOK IS NOT IN CATALOG\n')


def search_book():
    with pd.ExcelFile("lib.xlsx") as xls:
        df = pd.read_excel(xls, usecols=['name', 'author', 'year', 'genre'])
    enter_book_search = input('ENTER NAME, AUTHOR SEPARATE BY COMMA?\n')
    enter_book_search = enter_book_search.split(',')
    enter_book_search = list(map(lambda x: x.strip(), enter_book_search))
    enter_book_search = list(map(lambda x: x.lower(), enter_book_search))
    for i in enter_book_search:
        print(search(df, i))


def search(catalog, str_for_search=''):
    if len(str_for_search) == 0:
        print('ERROR\n')
        search_book()
    else:
        pos = 0
        counter = 0
        while pos in catalog.index:
            for i in catalog.iloc[pos]:
                j = str(i)
                j = j.lower()
                if j.find(str_for_search) != -1:
                    counter += 1
                    print(f'\n{catalog.iloc[pos]}')
            pos += 1
        if counter == 0:
            print('NOT FOUND INFO\n')
    return str("*"*36)


def main():
    action = False
    while not action:
        print("Main menu:\n"
              " 1 - Show books in catalog\n",
              "2 - Add book in catalog\n",
              "3 - Delete book\n",
              "4 - Search Book\n",
              "5 - Redact book\n",
              "6 - Exit from catalog\n"
              "Your action: ")
        act = int(input())
        try:
            act = int(act)
        except ValueError:
            print("Error")
            continue
        if act == 1:
            show_catalog()
            continue
        elif act == 2:
            add_book()
            continue
        elif act == 3:
            delete_book()
            continue
        elif act == 4:
            search_book()
            continue
        elif act == 5:
            input_redact()
            continue
        elif act == 6:
            action = True
            continue
        else:
            print("\nError")
            continue


if __name__ == '__main__':
    main()
