# Program that acts as a shopping cart for an online shopping website
# James Hughes 09/11/17

import random


def add_item(cart):

    # adds an item and quantity to the shopping cart

    item = input("What item would you like to add to your cart? : ")
    amount = float(input("How many would you like to add? : "))
    price = round(random.uniform(0, 20), 2)

    val = [amount, price]

    cart[item] = val

    return cart


def delete_item(cart):
    item = input("Which item would you like to remove from your cart? :")
    while True:

        if item in cart:
            del cart[item]
            return cart

        else:
            print("You do not have ", item, "in your cart")
            item = input("Please enter an item that is already in your cart :")



def change_quantity(cart):
    item = input("Which items quantity would you like to change? :")
    amount = int(input("Please enter the quantity you want to change it to :"))

    while True:

        if item in cart:
            cart[item][0] = amount
            return cart

        else:
            print("You do not have ", item, "in your cart")
            item = input("Please enter an item that is already in your cart :")
            amount = int(input("Please enter the quantity you want to change it to :"))



def display_cart(shopping_cart):

    # Displays the cart to the user / acts as a menu

    print('\n', 'Item     Quantity    Price')

    for x in shopping_cart:
        print('\n', x, '    ', end='')
        for y in shopping_cart[x]:
            print(y, '        ', end='')

    total(shopping_cart)
    print('\n\n1. Add item        2. Delete item')
    print('3. Change quantity\n')

def total(cart):

    # Calculates and displays the total price of the items in the cart

    total = 0
    for key in cart:
        total += (cart[key][0]) * (cart[key][1])

    print("\n\n            Total = ", total)
    return total

# start of program

shopping_cart = {'apple': [10, 1.25], 'bread': [1, 4.50]}
option = '0'

while True:
    if option == '0':
        display_cart(shopping_cart)
        option = input("please choose an option :")

    elif option == '1':
        shopping_cart = add_item(shopping_cart)
        option = '0'

    elif option == '2':
        shopping_cart = delete_item(shopping_cart)
        option = '0'

    elif option == '3':
        shopping_cart = change_quantity(shopping_cart)
        option = '0'

    elif option != '0' or option != '1' or option != '2' or option != '3':
        print("Please choose from menu")
        option = '0'
