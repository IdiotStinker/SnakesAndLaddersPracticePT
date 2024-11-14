from random import randint
board = []
def makeRandomBoard():
    global board
    board = [
        
    ]
    for row in range(10):
        board.append([""])
        for col in range(9):
            board[row].append("")

    #for row in board:
        #print(row)

    for row in range(10):
        for col in range(10):
            if row == 10 and col == 10:
                #If it is the last square, it will be blank.
                board[row][col] == " - "
                continue
            if row == 0 and col == 0:
                #If it is the first square, make it blank
                board[row][col] = " - "
                continue
            if not board[row][col] == "":
                #If the square has been defined it will remain the same. This is caused
                #when a ladder is made.
                continue
            rand = randint(1, 10)
            if rand == 1:
                #1/10 chance of snake
                snakeFall = randint(5, 15)
                #Add a zero so that the string lengths are the same for good printing.
                if snakeFall < 10:
                    board[row][col] = "-0" + str(snakeFall)
                else:
                    board[row][col] = "-" + str(snakeFall)
                #Write the square at the start then get rid of later if necessary.
                if snakeFall > row * 10 + col:
                    #If snakefall goes under the map.
                    board[row][col] = " - "
                    continue
                else:
                    #If the spot where the snake is leading is not a blank, undo the snake.
                    if board[int((10 * row + col - snakeFall) / 10)][(10 * row + col - snakeFall) % 10] == "" or board[int((10 * row + col - snakeFall) / 10)][(10 * row + col + snakeFall) % 10] == " - ":
                        #Set the square empty for future checking
                        board[int((10 * row + col - snakeFall) / 10)][(10 * row + col - snakeFall) % 10] = " - "
                        continue
                    else:
                        #If that square already has something, then undo the board.
                        board[row][col] = " - "
                        continue
            elif rand == 2:
                #1/10 chance of ladder
                ladderClimb = randint(5, 15)
                #(same as snake) Add a zero so that the string lengths are the same for good printing.
                if ladderClimb < 10:
                    board[row][col] = "+0" + str(ladderClimb)
                else:
                    board[row][col] = "+" + str(ladderClimb)
                #Write the square at the start then get rid of later if necessary.
                if ladderClimb + 10*row + col >= 100:
                    #If ladderClimb goes above the map.
                    board[row][col] = " - "
                    continue
                else:
                    #(same as snake) If the spot where the ladder is leading is not a blank, undo the ladder.
                    if board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] == "" or board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] == " - ":
                        #Set the square empty for future checking
                        board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] = " - "
                        continue
                    else:
                        #If the future square has something, return the current square empty.
                        board[row][col] = " - "
            else:
                #8/10 chances of blank
                board[row][col] = " - "

def startGame():
    try:
        global numOfPlayers
        numOfPlayers = int(input("How many people are playing? "))
        if (numOfPlayers > 4):
            print("Hey, too many. Four or less! ")
    except ValueError:
        print("Hey dude just input a number!!!")
        startGame()
        return

def playGame():
    p1 = -1
    p2 = -1
    p3 = -1
    p4 = -1
    global currentPlayer
    currentPlayer = 1
    global playing
    playing = True
    while(playing):
        userInput = input("Enter to roll or type 'end game' or 'resign' to do those or type 'board' to show the board. ").lower()
        #if userInput == "resign" or userInput == "end game":
            #do something
        
        if currentPlayer == 1:
            p1 = rollDice(p1)
        elif currentPlayer == 2:
            p2 = rollDice(p2)
        elif currentPlayer == 3:
            p3 = rollDice(p3)
        elif currentPlayer == 4:
            p4 = rollDice(p4)

        p1NonIndex = p1 + 1
        p2NonIndex = p2 + 1
        p3NonIndex = p3 + 1
        p4NonIndex = p4 + 1
    
        print(str(currentPlayer) + " " + str(p1NonIndex) + " " + str(p2NonIndex) + " " + str(p3NonIndex) + " " + str(p4NonIndex) + "\n")

        currentPlayer += 1
        if currentPlayer > numOfPlayers:
            currentPlayer = 1
    
    if currentPlayer == 1:
        currentPlayer = numOfPlayers
    else:
        currentPlayer -= 1

    print(f"Game Over! Player {currentPlayer} won the game! Wow, everyone else SUCKS in this game of skill.")


def rollDice(p):
    roll = randint(1, 6)
    if p + roll >= 99:
        global playing
        playing = False
        return p + roll
    return checkSquare(p + roll)

def checkSquare(newP):
    if not board[int(newP / 10)][newP % 10] == " - ":
        if "+" in board[int(newP / 10)][newP % 10]:
            climb = int(board[int(newP / 10)][newP % 10].split("+")[1])
            print(f"Player {currentPlayer} just hit a ladder and went up {climb} spaces!")
            return newP + climb
        elif "-" in board[int(newP / 10)][newP % 10]:
            fall = int(board[int(newP / 10)][newP % 10].split("-")[1])
            print(f"Player {currentPlayer} just slid down a snake {fall} squares!")
            return newP - fall
    else:
        return newP

def print_sol():
    #print(board)
    printBoard = board
    printBoard.reverse()
    #board.reverse()
    for index, row in enumerate(printBoard):

        #print(row)
        
        #coolRow = "".join(str(row).split("'"))

        if index % 2 == 0:
            coolRow = "".join(str(row).split("'"))
            print(coolRow)
        else:
            row.reverse()
            coolRow = "".join(str(row).split("'"))
            print(coolRow)

    #for rowNum, row in enumerate(board):
    #    if (rowNum % 2 == 1):
    #        print(row)
    #    else:
    #        print(row) 

makeRandomBoard()
print_sol()
startGame()
playGame()