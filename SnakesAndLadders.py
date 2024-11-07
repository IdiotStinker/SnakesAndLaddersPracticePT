from random import randint

def makeRandomBoard():
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
            if rand == 1:
                snakeFall = randint(5, 15)
                board[row][col] = "Snake " + str(snakeFall)
                if snakeFall > row * 10 + col:
                    board[row][col] = "Empty"
                    continue
                else:
                    if board[int((10 * row + col - snakeFall) / 10)][(10 * row + col - snakeFall) % 10].split()[0] == "Ladder" or board[int((10 * row + col - snakeFall) / 10)][(10 * row + col - snakeFall) % 10].split()[0] == "Snake":
                        board[row][col] = "Empty"
                    
            elif rand == 2:
                ladderClimb = randint(5, 15)
                board[row][col] = "Ladder " + str(ladderClimb)
                if ladderClimb + 10*row + col >= 100:
                    board[row][col] = "Empty"
                    continue
                else:
                    if board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10] == "":
                        continue
                    if board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10].split()[0] == "Ladder" or board[int((10 * row + col + ladderClimb) / 10)][(10 * row + col + ladderClimb) % 10].split()[0] == "Snake":
                        board[row][col] = "Empty"
            else:
                board[row][col] = "Empty"

    for rowNum, row in enumerate(board):
        if (rowNum % 2 == 1):
            print(row)
        else:
            print(row)

makeRandomBoard()