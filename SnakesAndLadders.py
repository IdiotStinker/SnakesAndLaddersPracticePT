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
                print(board[row][col])
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

def playGame():
    numOfPlayers = int(input("How many people are playing? "))
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    currentPlayer = 1
    playing = True
    while(playing):
        userInput = input("Enter to roll or type 'end game' or 'resign' to do those. ").lower()
        #if userInput == "resign" or userInput == "end game":
            #do something
        
        if currentPlayer == 1:
            rollDice(p1)
        elif currentPlayer == 2:
            rollDice(p2)
        elif currentPlayer == 3:
            rollDice(p3)
        elif currentPlayer == 4:
            rollDice(p4)
    
        print(str(currentPlayer) + " " + str(p1) + " " + str(p2) + " " + str(p3) + " " + str(p4))

        currentPlayer += 1
        if currentPlayer > numOfPlayers:
            currentPlayer = 1


        

def rollDice(p):
    roll = randint(1, 6)
    p += roll
    checkSquare(p)

def checkSquare(p):
    if not board[int(p / 10)][p % 10] == " - ":
        if "+" in board[int(p / 10)][p % 10]:
            p += int(board[int(p / 10)][p % 10].split("+")[1])
        elif "-" in board[int(p / 10)][p % 10]:
            p -= int(board[int(p / 10)][p % 10].split("-")[1])
        return
    else:
        return

def print_sol():
    #print(board)
    for row in board:

        #print(row)
        coolRow = "".join(str(row).split("'"))


        print(coolRow)

    #for rowNum, row in enumerate(board):
    #    if (rowNum % 2 == 1):
    #        print(row)
    #    else:
    #        print(row) 

makeRandomBoard()
print_sol()
playGame()

cool = " +4".split("+")
print(cool)