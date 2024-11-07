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
            if board[row][col] == "Empty":
                print(board[row][col])
                continue
            rand = randint(1, 10)
            if rand == 1:
                snakeIncrease = randint(5, 15)
                board[row][col] = "Snake " + str(snakeIncrease)
                if snakeIncrease > row * 10 + col:
                    board[row][col] = ""
                    continue
                else:
                    if board[int((10 * row + col - snakeIncrease) / 10)][(10 * row + col - snakeIncrease) % 10].split()[0] == "Ladder" or board[int((10 * row + col - snakeIncrease) / 10)][(10 * row + col - snakeIncrease) % 10].split()[0] == "Snake":
                        board[row][col] = "Empty"
                    
            elif rand == 2:
                board[row][col] = "Ladder " + str(randint(5, 15))
                if int(board[row][col].split()[1]) > 100 - (row * 10 + col):
                    board[row][col] = ""
            else:
                board[row][col] = ""

    for row in board:
        print(row)

makeRandomBoard()