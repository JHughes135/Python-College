import random


class randNo (object):

    def __init__(self):

        self.randNo = random.randint(1, 100)


random = randNo()

notWon = True

while notWon:

    guess = input("Please enter your guess: ")

    guess = int(guess)

    if guess > random.randNo:
        print("too high")

    if guess < random.randNo and guess > 0:
        print("too low")

    if guess == 0:
        print("goodbye")
        break

    if guess == random.randNo:
        print("well done!")
        notWon = False







