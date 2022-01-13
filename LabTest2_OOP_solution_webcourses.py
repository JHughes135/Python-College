# Sample Solution for OOP Lab Test 2
#
# This program uses a dictionary to save the book list information
# The key is the ID
# Make sure to include error-checking where appropriate, this sample solution shows the general approach only

# reads list of books from a file and stores them in a dictionary
def read_books():
    books_dict = {}
    try:
        file_obj = open("books.txt", "r")
        for line in file_obj:
            line = line.strip()
            process_line(line, books_dict)
        file_obj.close()

        return books_dict

    except IOError:
        print("Problem with file.")
        return {}


def save_to_file(dict):
    try:
        file_obj = open("booksOut.txt", "w")
        for key in dict.keys():
            line = str(key) + "," + dict[key][0] + "," + dict[key][1] + "," + str(dict[key][2]) + "\n"
            file_obj.write(line)

        file_obj.close()

    except IOError:
        print("Problem with file.")
        return {}


def process_line(line, dict):
    list = line.split(",")
    # print(list)
    id = int(list[0])
    title = list[1]
    author = list[2]
    price = float(list[3])
    dict[id] = [title, author, price]
    return dict


def add_book(dict):
    id = int(input("Please enter ID: "))
    title = input("Please enter title: ")
    author = input("Please enter author: ")
    price = float(input("Please enter price: "))
    dict[id] = [title, author, price]
    return dict


def find_author(title, dict):
    for value in dict.values():
        if value[0] == title:
            return value[1]

    return None


def find_price(title, dict):
    for value in dict.values():
        if value[0] == title:
            return value[2]

    return None


def calculate_total_price(dict):
    total = 0
    for value in dict.values():
        total = total + value[2]

    return total

def apply_discount(dict):
    for value in dict.values():
        value[2] = value[2]*0.9

    return dict

# print info about all books
# if you'd like to format the price nicely to 2 digits after decimal point, you can use string format with "%.2f"
def print_books(dict):
    for key in dict.keys():
        print("ID: " + str(key) + ", Title: " + dict[key][0] + ", Author: " + dict[key][1] + ", Price:" + str(
            dict[key][2]))


def menu():
    print("Welcome to our book management system. Please choose from the following options:")
    print("1. Read list of books from a file")
    print("2. Save list of books to a file")
    print("3. Add a new book")
    print("4. Search for author by book title")
    print("5. Calculate total price")
    print("6. Apply 10% discount")
    print("7. Print all books")
    print("8. Exit")
    choice = int(input())
    return choice


# main part of the program
# make sure you include error checking, etc...


