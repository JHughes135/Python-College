#Program to sort a list from lowest number to highest


sortl = []

for i in range(1, 8):

    i = input("enter numbers to sort: ")

    sortl.append(i)



def bubble(list_sort):
    length = len(list_sort)
    sorted = False

    for j in range(length):

        for k in range(0, length-i-1):

            if list_sort[j] > list_sort[j + 1]:
                list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]


bubble(sortl)
print(sortl)
