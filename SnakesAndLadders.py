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
                board[row][col] = "    Empty"
                continue
            if rand == 1:
                snakeFall = randint(5, 15)
                if snakeFall < 10:
                    board[row][col] = "Snake  0" + str(snakeFall)
                else:
                    board[row][col] = "Snake  " + str(snakeFall)
                if snakeFall > row * 10 + col:
                    board[row][col] = "    Empty"
                    continue
                else:
                    if board[int((10 * row + col - snakeFall) / 10)][(10 * row + col - snakeFall) % 10] == "" or board[int((10 * row + col - snakeFall) / 10)][(10 * row + col + snakeFall) % 10] == "Empty":
                        continue
                    else:
                        board[row][col] = "    Empty"
                        continue
                    
            elif rand == 2:
                ladderClimb = randint(5, 15)
                if ladderClimb < 10:
                    board[row][col] = "Ladder 0" + str(ladderClimb)
                else:
                    board[row][col] = "Ladder " + str(ladderClimb)
                if ladderClimb + 10*row + col >= 100:
                    board[row][col] = "    Empty"
                    continue
                else:
                    if board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] == "" or board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] == "Empty":
                        continue
                    else:
                        board[row][col] = "    Empty"
            else:
                board[row][col] = "    Empty"

    



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