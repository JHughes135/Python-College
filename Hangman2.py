# Hangman
# Player 1 will enter a word, then player 2 will have 5 attempts
# to guess the letters in that word



play = "y"

while play == "y":

    def progress(guess, word):
        for n in word:
            word.remove(guess)

        return word


    Guesses = 0
    Lives = 10

    word = input("Player 1, Please enter your word: ")
    word = word.lower()
    word = list(word)
    word_backup = word

    while Lives > 0 and len(word) > 0:
        print("The Word is",len(word), "leters long")
        Guess = input("Guess a letter: ")

        if Guess in word:
            word = progress(Guess, word)
            print(word)

        else:
            Lives -= 1
            print(Lives, "lives left")

            if Lives == 0:
                play = input("Game Over, play again? y/n: ")

    if len(word) < 1:
        print("You win!!")
        play = input("Play again? y/n:")

while play != "y" and play != "n":
    print("Please enter y or n!")
    play = input("Play again? : ")

    if play == "y":
        break
    if play == "n":
        break

if play == "n":
    print("Goodbye")
