from random import randint
green = "\033[92m"
black = "\033[47m"
def makeRandomBoard():
    global board
    board = []
    #Necessary for making the board without manually doing it.
    for row in range(10):
        board.append([""])
        for col in range(9):
            board[row].append("")

    #for row in board:
        #print(row)

    for row in range(10):
        for col in range(10):
            if row == 9 and col == 9:
                #If it is the last square, it will be blank.
                board[row][col] = "END"
                break
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
                if ladderClimb + 10*row + col >= 99:
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
    #Try block catching non numeric inputs.
    try:
        global numOfPlayers
        #Get the player count
        numOfPlayers = int(input("How many people are playing? "))
        #Four or less players only
        if numOfPlayers > 4:
            print("Hey, too many. Four or less! ")
            #Start game to run this function again.
            startGame()
            return
        if numOfPlayers < 0:
            print("Hey I can't play with negative players.")
            startGame()
            return
        if numOfPlayers == 0:
            #Different print message
            print("Wow a zero player game, sounds like a party")
            startGame()
            return
    except ValueError:
        #Inform player and ask again for player count
        print("Hey dude just input a number!!!")
        startGame()
        return

def playGame():
    #This is off the board, which is where the player starts.
    #They are global for the printing board
    global p1
    p1 = -1
    global p2
    p2 = -1
    global p3
    p3 = -1
    global p4
    p4 = -1
    global currentPlayer
    #Player 1 starts
    currentPlayer = 1
    global playing
    #We start playing
    playing = True
    resignedPlayers = []
    while(playing):
        if currentPlayer in resignedPlayers:
            #Skip their turn permanently
            currentPlayer += 1
            if currentPlayer > numOfPlayers:
                currentPlayer = 1
            continue
        #If the user wants something he can get it
        userInput = input(f"Hey Player {currentPlayer}, enter to roll or type 'end game' or 'resign' to do those or type 'board' to show the board. ").lower()
        #If a player is a loser he can give up and make him out of the game
        if userInput == "resign":
            resignedPlayers.append(currentPlayer)
            #If everyone is resigned then the game ends
            if len(resignedPlayers) == numOfPlayers:
                playing = False
            else:
                continue
        #Ends the game for all players
        if userInput == "end game" or not playing:
            #make a list of all players
            playerList = [p1, p2, p3, p4]
            #Find the largest of the positions the players are at
            #Then find that spot plus one which corresponds to that player
            currentPlayer = playerList.index(max(playerList)) + 1
            playing = False
            continue
        if userInput == "board":
            printBoard()
            continue
        if not userInput == "":
            #If the user typo or try some other command
            print("You didn't do anything, here's your turn again")
            continue
        
        #Play the corresponding player's turn
        if currentPlayer == 1:
            p1 = rollDice(p1)
        elif currentPlayer == 2:
            p2 = rollDice(p2)
        elif currentPlayer == 3:
            p3 = rollDice(p3)
        elif currentPlayer == 4:
            p4 = rollDice(p4)

        #The index position is always one less, these make it easier for players to understand.
        p1NonIndex = p1 + 1
        p2NonIndex = p2 + 1
        p3NonIndex = p3 + 1
        p4NonIndex = p4 + 1
    
        #Showing current player and each individual's position
        print(str(currentPlayer) + " " + str(p1NonIndex) + " " + str(p2NonIndex) + " " + str(p3NonIndex) + " " + str(p4NonIndex) + "\n")

        #For the last roll we shouldn't change current player
        if playing:
        #Change the player's turn, if it is above the number of players then it is again player one's turn
            currentPlayer += 1
        #Here if the current player was about num of players.
            if currentPlayer > numOfPlayers:
                currentPlayer = 1
        
    #Game Over message
    print(f"Game Over! Player {currentPlayer} won the game! Wow, everyone else SUCKS in this game of skill.")


def rollDice(p):
    #A dice with the imported random.randint
    roll = randint(1, 6)
    print(f"Player {currentPlayer} rolled a {roll}!")
    #Helpful for player and me
    if p + roll >= 99:
        #If it gets to final square, the game is over!
        global playing
        playing = False
        return p + roll
    #Return the new value that checkSquare returns.
    #This will calculate a change if there is a ladder or snake
    return checkSquare(p + roll)

def checkSquare(newP):
    #If the spot is not blank:
    if not board[int(newP / 10)][newP % 10] == " - ":
        #Find if it is a snake or ladder:
        if "+" in board[int(newP / 10)][newP % 10]:
            #Then move player by the number
            climb = int(board[int(newP / 10)][newP % 10].split("+")[1])
            print(f"\033[92mPlayer {currentPlayer} just hit a ladder and went up {climb} spaces!\033[0m")
            #This value returns to the top and changes the current player
            return newP + climb
        elif "-" in board[int(newP / 10)][newP % 10]:
            #Then move player by the number
            fall = int(board[int(newP / 10)][newP % 10].split("-")[1])
            print(f"\033[92mPlayer {currentPlayer} just slid down a snake {fall} squares!\033[0m")
            #This value returns to the top and changes the current player
            return newP - fall
    else:
        #Otherwise just keep the spot
        return newP

def printBoard(start = False):
    #print(board)
    printBoard = []
    #Create a fresh board for printing
    for index, row in enumerate(board):
        if index % 2 == 0:
            #Make row not affected by printRow, so make it not related to row
            printRow = []
            for i in row:
                printRow.append(i)
            if not start:
                #OK, so if we are in the right row (pos / 10 rounded down) then put then set the remainder as the player's name
                if int(p1 / 10) == index:
                    printRow[p1 % 10] = " P1"
                #Also make sure that that many players are playing
                if int(p2 / 10) == index and numOfPlayers >= 2:
                    printRow[p2 % 10] = " P2"
                if int(p3 / 10) == index and numOfPlayers >= 3:
                    printRow[p3 % 10] = " P3"
                if int(p4 / 10) == index and numOfPlayers >= 4:
                    printRow[p4 % 10] = " P4"
                
            #Add it to the board made for printing
            printBoard.append(printRow)
        else:
            #Create a new row for reversing
            printRow = []
            for i in row:
                printRow.append(i)
            #First board print wont have the players defined.
            if not start:
                #OK, so if we are in the right row (pos / 10 rounded down) then put then set the remainder as the player's name
                if int(p1 / 10) == index:
                    printRow[p1 % 10] = " P1"
                #Also make sure that that many players are playing
                if int(p2 / 10) == index and numOfPlayers >= 2:
                    printRow[p2 % 10] = " P2"
                if int(p3 / 10) == index and numOfPlayers >= 3:
                    printRow[p3 % 10] = " P3"
                if int(p4 / 10) == index and numOfPlayers >= 4:
                    printRow[p4 % 10] = " P4"

            #Flip every other row for authentic Snakes and Ladders gameplay!
            printRow.reverse()
            #Add it to the board made for printing
            printBoard.append(printRow)

    printBoard.reverse()
    #Reverse so the top is the end and bottom is the start

    for index, row in enumerate(printBoard):
        #Get rid of the apostrophe
        coolRow = "".join(str(row).split("'"))
        #Helpful directional arrows!
        if index % 2 == 0:
            print(coolRow + "<---")
        else:
            print(coolRow + "--->")

    #Add a seperating line
    print("\n")



list = ["\033[0m 0;30;47mhey my name jeff", "no", 19]
print(list)
#Making a random board for infinite playtime!
makeRandomBoard()
#Showing the board off rip
printBoard(True)
#Start game there to ask how many players
startGame()
#Play game loop, runs the game. There is a while loop which goes until the game is done.
playGame()