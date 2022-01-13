def read_books():
    try:
        file = open("books.txt", "r")
        for line in file:
            line = line.strip()
            process_line(line, books_dict)
        file.close()

        return books_dict

    except IOError:
        print('Problem with file!!')
        return {}


def process_line(line, dict):
    list = line.split(",")
    id = list[0]
    title = list[1]
    author = list[2]
    price = list[3]
    print(list)


def add_book (dict):



def menu():
    print("\n James's Book Management System\n")
    print(" 1. Add book\n")
    print(" 2. Search for Author by title.\n")
    print(" 3. Print book catalogue.\n")
    print(" 4. Total price.\n")
    print(" 5. Apply 10% discount.\n")
    print(" 6. Save book list to file\n")
    print("Please choose an option : ")
    choice = int(input())

    return choice

books_dict = {}ist
menu()
read_books()
