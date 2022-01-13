# Program to implement the game of X's and O's
# James Hughes 03/11/17

import random


def drawBoard(board):
    # This function prints the board to the screen

    print('   |   |')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    # Lets the player choose X or O and sets computer to opposite
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("would you like to play as X's or O's? : X/O")
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose who goes first

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Returns true is move is free
    return board[move] == ''


def getPlayerMove(board):
    move = ''
    while move not in ' 1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moveslist):
    # Returns valid move from the passed list on the passed board.
    possibleMoves = []
    for i in moveslist:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # TIC TAC TOE AI

    # Checks if computer can win on next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Checks if player can win on next move, and blocks them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners if free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take centre, if it is free
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# !!!!!!!!!!!!!!!!!!
# START OF PROGRAM


print("Welcome to TIC TAC TOE!")

while True:
    # reset the board
    theBoard = [''] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn, "will go first")

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # players turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Congratulations, You Win!!!")
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"

        else:
            # computers turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("You lose :(")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Its a Tie")
                else:
                    turn = "player"

    if not playAgain():
        break
