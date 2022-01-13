import random

class Item(object):

    _registry = []

    def __init__(self, name):
        self.item_name = name
        self.item_price = round(random.uniform(0, 20), 2)
        self.item_quantity = int(input("How many would you like to add? : "))
        self._registry.append(self)

    def __str__(self):
        return "{}   {}      {}".\
        format(self.item_name, self.item_price, self.item_quantity)


def add_item():

    item_name = input("What item would you like to add to your cart? : ")
    item_name = Item(item_name)


def remove_item():
    item = input("Which item would you like to remove? : ")
    Item._registry.remove(item)


def display_cart():
    for p in Item._registry:
        print(p,"\n")
    total()


def total():

    # Calculates and displays the total price of the items in the cart

    total = 0
    for p in Item._registry:
        total += (p.item_price) * (p.item_quantity)


    print("\n\n            Total = ", total)
    return total



option = '0'

while True:

    if option == '0':
        dir(Item)
        display_cart()
        option = input("please choose an option :")

    elif option == '1':
        objects = add_item()
        option = '0'

    elif option == '2':
        remove_item()
        option = '0'