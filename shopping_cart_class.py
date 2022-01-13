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


def add_item(list):

    item_name = input("What item would you like to add to your cart? : ")
    item_name = Item(item_name)
    list.append(item_name)

    return list


def display_cart(objects):
    for i in range(0, len(objects)):
        print(objects[i])
        total_price = total()


def total():

    # Calculates and displays the total price of the items in the cart

    total = 0
    for p in Item._registry:
        total += (p.item_price) * (p.item_quantity)

    print("\n\n            Total = ", total)
    return total


objects = []
option = '0'

while True:

    if option == '0':
        display_cart(objects)
        option = input("please choose an option :")

    elif option == '1':
        objects = add_item(objects)
        option = '0'

    elif option == '2':
        objects = add_item(objects)
        option = '0'
