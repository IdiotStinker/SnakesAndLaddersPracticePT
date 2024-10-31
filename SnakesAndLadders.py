from random import randint

def makeRandomBoard():
    board = [
        ["",]
    ]
    for row in range(10):
        for col in range(10):
            if board[row][col] != "":
                return
            rand = randint(1, 10)
            if rand == 1:
                board[row]
            board[row][col] = 

