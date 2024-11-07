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
            if not board[row][col] == "":
                print(board[row][col])
                continue
            rand = randint(1, 10)
            if row == 0 and col == 0:
                board[row][col] = " - "
                continue
            if rand == 1:
                #1/10 chance of snake
                snakeFall = randint(5, 15)
                #Add a zero so that the string lengths are the same for good printing.
                if snakeFall < 10:
                    board[row][col] = "-0" + str(snakeFall)
                else:
                    board[row][col] = "-" + str(snakeFall)
                if snakeFall > row * 10 + col:
                    board[row][col] = " - "
                    continue
                else:
                    #If the spot where the snake is leading is not a blank, undo the snake.
                    if board[int((10 * row + col - snakeFall) / 10)][(10 * row + col - snakeFall) % 10] == "" or board[int((10 * row + col - snakeFall) / 10)][(10 * row + col + snakeFall) % 10] == " - ":
                        continue
                    else:
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
                if ladderClimb + 10*row + col >= 100:
                    board[row][col] = " - "
                    continue
                else:
                    #(same as snake) If the spot where the ladder is leading is not a blank, undo the ladder.
                    if board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] == "" or board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] == " - ":
                        continue
                    else:
                        board[row][col] = " - "
            else:
                #8/10 chances of blank
                board[row][col] = " - "

    



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
#cool()